import pandas as pd
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import Tuple
import os
import logging

@dataclass
class DataFrames:
    contact_df: pd.DataFrame
    marketing_df: pd.DataFrame
    sales_df: pd.DataFrame
    opportunity_df: pd.DataFrame

def import_data() -> DataFrames:
    base_path = os.path.join(os.getcwd(), 'datasets', 'input')
    contact_df = pd.read_excel(os.path.join(base_path, 'de_hw_contact_data.xlsx'))
    marketing_df = pd.read_csv(os.path.join(base_path, 'de_hw_marketing_data.csv'))
    sales_df = pd.read_csv(os.path.join(base_path, 'de_hw_sales_outreach_data.csv'))
    opportunity_df = pd.read_csv(os.path.join(base_path, 'de_hw_opportunity_data.csv'))
    return DataFrames(contact_df, marketing_df, sales_df, opportunity_df)

def merge_touchpoint_data(marketing_df: pd.DataFrame, sales_df: pd.DataFrame) -> pd.DataFrame:
    marketing_df['touchpoint_type'] = 'marketing'
    marketing_df = marketing_df.rename(columns={
        'marketing_touchpoint_id': 'touchpoint_id',
        'marketing_touchpoint_date': 'touchpoint_date'
    })
    sales_df['touchpoint_type'] = 'sales'
    sales_df = sales_df.rename(columns={
        'sales_touchpoint_id': 'touchpoint_id',
        'sales_touchpoint_date': 'touchpoint_date'
    })
    return pd.concat([marketing_df, sales_df], ignore_index=True)


def join_data(touchpoint_df: pd.DataFrame, contact_df: pd.DataFrame, opportunity_df: pd.DataFrame) -> pd.DataFrame:
    merged_df = touchpoint_df.merge(contact_df, on='contact_id', how='left')
    merged_df = merged_df.merge(opportunity_df, on='account_id', how='inner')
    return merged_df

def filter_touchpoints(df: pd.DataFrame) -> pd.DataFrame:
    df['Opportunity_Created_Date'] = pd.to_datetime(df['Opportunity_Created_Date'])
    df['touchpoint_date'] = pd.to_datetime(df['touchpoint_date'])
    df['days_before_opp'] = (df['Opportunity_Created_Date'] - df['touchpoint_date']).dt.days
    return df[df['days_before_opp'].between(0, 90)]

def identify_first_touch(df: pd.DataFrame) -> pd.DataFrame:
    df_sorted = df.sort_values(['opportunity_id', 'touchpoint_date'])
    first_touch = df_sorted.groupby('opportunity_id').first().reset_index()
    return first_touch

def calculate_sourced_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    df['Sourced_Pipeline'] = df['pipeline_amount']
    return df

def create_output_table(df: pd.DataFrame) -> pd.DataFrame:
    columns = [
        'touchpoint_id', 'channel_name', 'contact_id', 'account_id', 'opportunity_id',
        'touchpoint_date', 'Opportunity_Created_Date', 'pipeline_amount', 'Sourced_Pipeline',
        'sales_segment'
    ]
    return df[columns]

def validate_data(df: pd.DataFrame) -> None:

    # Duplicate checks
    if df.duplicated(subset=['opportunity_id']).any():
        raise ValueError("Duplicate opportunities found.")
    
    # Null checks
    critical_columns = ['channel_name', 'opportunity_id', 'pipeline_amount']
    if df[critical_columns].isnull().any().any():
        raise ValueError("Null values found in critical columns.")
    
    # Consistency checks
    if not (df['touchpoint_date'] <= df['Opportunity_Created_Date']).all():
        raise ValueError("Inconsistent touchpoint dates found.")
    
    # Aggregated data validation
    aggregated_pipeline = df.groupby('channel_name')['Sourced_Pipeline'].sum()
    if not aggregated_pipeline.equals(df.groupby('channel_name')['pipeline_amount'].sum()):
        raise ValueError("Aggregated pipeline amounts do not match source data.")

def main() -> None:
    try:
        # Import data
        data = import_data()
        
        # Process data
        touchpoint_df = merge_touchpoint_data(data.marketing_df, data.sales_df)
        merged_df = join_data(touchpoint_df, data.contact_df, data.opportunity_df)
        filtered_df = filter_touchpoints(merged_df)
        first_touch_df = identify_first_touch(filtered_df)
        pipeline_df = calculate_sourced_pipeline(first_touch_df)
        
        # Validate data
        validate_data(pipeline_df)
        
        # Create final output
        output_df = create_output_table(pipeline_df)
        
        # Save to CSV
        base_path = os.path.join(os.getcwd(), 'datasets', 'output')
        output_df.to_csv(os.path.join(base_path, 'attribution_output.csv'), index=False)
        logging.info("Output saved to CSV successfully.")
        
        # Basic analysis
        channel_pipeline = output_df.groupby('channel_name')['Sourced_Pipeline'].sum().sort_values(ascending=False)
        print("Pipeline sourced by channel:")
        print(channel_pipeline)
        
        segment_channel_pipeline = output_df.pivot_table(
            values='Sourced_Pipeline', 
            index='sales_segment', 
            columns='channel_name', 
            aggfunc='sum'
        )
        print("\nPipeline sourced by channel and sales segment:")
        print(segment_channel_pipeline)
    except Exception as e:
        logging.error(f"An error occurred in the main process: {e}")

if __name__ == "__main__":
    main()