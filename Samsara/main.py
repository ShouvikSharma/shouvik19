import pandas as pd
from datetime import datetime, timedelta
import openpyxl

# Step 1: Import data
def import_data():
    contact_df = pd.read_excel('de_hw_contact_data.xlsx')
    marketing_df = pd.read_csv('de_hw_marketing_data.csv')
    sales_df = pd.read_csv('de_hw_sales_outreach_data.csv')
    opportunity_df = pd.read_csv('de_hw_opportunity_data.csv')
    return contact_df, marketing_df, sales_df, opportunity_df

# Step 2: Merge marketing and sales data
def merge_touchpoint_data(marketing_df, sales_df):
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
    
    touchpoint_df = pd.concat([marketing_df, sales_df], ignore_index=True)
    return touchpoint_df

# Step 3: Join touchpoint data with contact and opportunity data
def join_data(touchpoint_df, contact_df, opportunity_df):
    merged_df = touchpoint_df.merge(contact_df, on='contact_id', how='left')
    merged_df = merged_df.merge(opportunity_df, on='account_id', how='inner')
    return merged_df

# Step 4: Filter touchpoints within 90 days before opportunity creation
def filter_touchpoints(df):
    df['Opportunity_Created_Date'] = pd.to_datetime(df['Opportunity_Created_Date'])
    df['touchpoint_date'] = pd.to_datetime(df['touchpoint_date'])
    df['days_before_opp'] = (df['Opportunity_Created_Date'] - df['touchpoint_date']).dt.days
    return df[df['days_before_opp'].between(0, 90)]

# Step 5: Identify first touchpoint for each opportunity
def identify_first_touch(df):
    df_sorted = df.sort_values(['opportunity_id', 'touchpoint_date'])
    first_touch = df_sorted.groupby('opportunity_id').first().reset_index()
    return first_touch

# Step 6: Calculate sourced pipeline
def calculate_sourced_pipeline(df):
    df['Sourced_Pipeline'] = df['pipeline_amount']
    return df

# Step 7: Create final output table
def create_output_table(df):
    columns = [
        'touchpoint_id', 'channel_name', 'contact_id', 'account_id', 'opportunity_id',
        'touchpoint_date', 'Opportunity_Created_Date', 'pipeline_amount', 'Sourced_Pipeline',
        'sales_segment'
    ]
    return df[columns]

# Main function to run the entire process
def main():
    # Import data
    contact_df, marketing_df, sales_df, opportunity_df = import_data()
    
    # Process data
    touchpoint_df = merge_touchpoint_data(marketing_df, sales_df)
    merged_df = join_data(touchpoint_df, contact_df, opportunity_df)
    filtered_df = filter_touchpoints(merged_df)
    first_touch_df = identify_first_touch(filtered_df)
    pipeline_df = calculate_sourced_pipeline(first_touch_df)
    
    # Create final output
    output_df = create_output_table(pipeline_df)
    
    # Save to CSV
    output_df.to_csv('attribution_output.csv', index=False)
    
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

main()
# if __name__ == "__main__":
#     main()