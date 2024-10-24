import pandas as pd
from sqlalchemy import create_engine

# Load the dataset
df = pd.read_csv('online_retail.csv', encoding='unicode_escape')

# Data cleaning
# Drop rows with missing CustomerID
df.dropna(subset=['CustomerID'], inplace=True)

# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Filter out negative quantities
df = df[df['Quantity'] > 0]

# Connect to PostgreSQL
engine = create_engine('postgresql+psycopg2://user:password@db:5432/airflow')

# Load DataFrame to PostgreSQL
df.to_sql('online_retail', engine, if_exists='replace', index=False)

print("Data loaded successfully into PostgreSQL!")
