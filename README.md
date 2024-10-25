# ETLPipelineWithDocker
This project presents a Bike Sales Dashboard in Excel, providing a comprehensive analysis of sales data across key dimensions like date, segment, country, and product. The interactive dashboard enables stakeholders to monitor performance metrics and make data-driven decisions easily.

## Key Features
- Data Ingestion: Extract data and load it into a data warehouse.

- Data Transformation: Clean and transform data using Python scripts to prepare it for analysis.

- Workflow Automation: Use Apache Airflow to orchestrate data workflows, ensuring seamless ETL processes.

- Containerization: Utilize Docker to create isolated environments for the application, enhancing portability and scalability.

## Technologies Used:
- Python
- Apache Airflow
- Docker
- SQL
- Online Retail Dataset

## Dataset Analysis and Visualizations
### 1. Revenue Over Time

Analyzing revenue at different intervals—daily, weekly, and monthly—helps us capture both short- and long-term sales trends.
- Daily Revenue Trend: This analysis highlights fluctuations in revenue on a daily basis, helping identify specific days with high or low sales due to short-term events.
- Weekly Revenue Trend: Weekly revenue smoothing provides insights into consistent trends and mitigates the impact of daily fluctuations.
- Monthly Revenue Trend: Monthly patterns show seasonal shifts and long-term growth trends, useful for strategic planning.

### 2. Customer Analysis

This analysis focuses on understanding customer purchasing behavior, which includes:
- Top Buyers: Identify the top customers by total revenue, showing which customers are the most valuable.
- Return Frequency: Track how frequently customers return to make additional purchases.
- Average Spend: Calculate the average amount spent per customer, helping categorize high, medium, and low spenders.

### 3. Returns Analysis

Analyzing product returns helps us understand the impact of returned items on revenue:
- eturn Rate: Calculate the total value of returned products relative to sales, which can highlight quality or fulfillment issues.
- Frequent Returners: Identify customers or products associated with high return rates, providing insights for product or service improvements.

### 4. Time-Series Trends

This analysis provides insights into recurring sales patterns over time, capturing both seasonal and cyclical trends:
- Daily Patterns: Examine day-to-day changes in sales volume.
- Weekly and Monthly Patterns: Explore longer trends that may correlate with holiday seasons or special events.
