
# Attribution System Analysis

## Overview

This project implements a basic attribution system for analyzing the impact of marketing and sales touchpoints on pipeline generation. It processes data from various sources, applies a first-touch attribution model, and provides insights into channel performance across different sales segments.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Data Files](#data-files)
4. [System Architecture](#system-architecture)
5. [Attribution Logic](#attribution-logic)
6. [Output](#output)
7. [Analysis](#analysis)
8. [Data Validation](#data-validation)
9. [Future Enhancements](#future-enhancements)
10. [Contributing](#contributing)
11. [License](#license)

## Overview
This manual provides detailed instructions on how to use the Python script designed for processing data in the Samsara project. The script automates data import, merging, validation, and filtering to ensure data integrity and consistency.

## Setup

These installation instructions assume that you have [Python 3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/cli/pip_install/) installed.

### 1. Clone this repository

```bash
cd && git clone https://github.com/shouvik19/Samsara.git
```

### 2. Go to the root of the directory

```bash
cd Samsara
```
### 3. Create a Python virtual environment

```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

### Running the Script

```bash
python main.py
```
## Usage

1. Ensure your data files are in the project directory (see [Data Files](#data-files) section).

2. Run the main script:

3. Check the console output for summary statistics and the `attribution_output.csv` file for detailed results.

## Data Files

Ensure the following files are present in the project directory:

- `de_hw_contact_data.xlsx`: Contact data (Excel format)
- `de_hw_marketing_data.csv`: Marketing touchpoint data
- `de_hw_sales_outreach_data.csv`: Sales touchpoint data
- `de_hw_opportunity_data.csv`: Opportunity data

## System Architecture

The system follows these main steps:

1. Data Ingestion: Read data from Excel and CSV files
2. Data Merging: Combine touchpoint data and join with contact/opportunity data
3. Data Processing: Apply attribution logic and calculate sourced pipeline
4. Analysis: Aggregate results and generate insights

## Attribution Logic

- Attribution Window: 90 days before opportunity creation
- Attribution Model: First-touch (first touchpoint within the window gets full credit)

## Output

The script generates two main outputs:

1. Console output: Summary statistics of pipeline sourced by channel and sales segment
2. `attribution_output.csv`: Detailed attribution data for further analysis

## Analysis

The system provides insights into:

- Channel performance: Which channels source the most pipeline
- Segmented analysis: How channel performance varies across sales segments
- Time-based analysis: Understanding the time from first touch to opportunity creation

## Data Validation

To ensure data quality, implement the following checks:

- Data completeness: Check for missing values in critical fields
- Data consistency: Ensure logical relationships (e.g., touchpoint dates before opportunity creation)
- Business logic: Verify attribution calculations and totals
- Cross-system reconciliation: Compare with source systems (CRM, marketing platforms)

## Future Enhancements

1. Implement multi-touch attribution models
2. Incorporate cost data for ROI calculations
3. Develop real-time attribution capabilities
4. Create interactive dashboards for stakeholders
5. Implement machine learning for predictive attribution

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

For any questions or support, please contact [shouvik19@gmail.com](mailto:shouvik19@gmail.com).