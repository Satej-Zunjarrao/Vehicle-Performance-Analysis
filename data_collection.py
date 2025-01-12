# data_collection.py
# This script handles the ingestion of telematics data from various sources like SQL databases and flat files.
# The primary objective is to retrieve the raw vehicle performance data and prepare it for subsequent cleaning and analysis.

import pandas as pd
import sqlite3  # Assuming SQLite for the SQL database connection
import os

# Define paths to the data sources
SQL_DATABASE_PATH = "C:/Users/Satej/Documents/Vehicle_Telematics/vehicle_data.db"
CSV_FILE_PATH = "C:/Users/Satej/Documents/Vehicle_Telematics/vehicle_performance_data.csv"

# Function to connect to SQL database and retrieve data
def fetch_data_from_sql(query: str):
    """
    Connects to the SQL database and executes the provided SQL query to retrieve the data.
    
    Parameters:
    query (str): SQL query to retrieve the desired data from the database.
    
    Returns:
    pd.DataFrame: A Pandas DataFrame containing the result of the query.
    """
    try:
        # Establish connection to the SQL database
        conn = sqlite3.connect(SQL_DATABASE_PATH)
        print("Successfully connected to the SQL database.")
        
        # Fetch data using the provided query
        data = pd.read_sql(query, conn)
        conn.close()
        
        print(f"Data retrieved successfully from SQL database.")
        return data
    except Exception as e:
        print(f"Error fetching data from SQL: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error

# Function to read data from CSV file
def fetch_data_from_csv():
    """
    Reads the telematics data stored in a CSV file and returns it as a Pandas DataFrame.
    
    Returns:
    pd.DataFrame: A Pandas DataFrame containing the data from the CSV file.
    """
    try:
        # Check if the file exists
        if os.path.exists(CSV_FILE_PATH):
            data = pd.read_csv(CSV_FILE_PATH)
            print("Data successfully loaded from CSV file.")
            return data
        else:
            print(f"Error: CSV file not found at {CSV_FILE_PATH}")
            return pd.DataFrame()
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return pd.DataFrame()

# Main function to collect data
def collect_data():
    """
    Collects data from multiple sources (SQL database and CSV file) and merges them for further processing.
    
    Returns:
    pd.DataFrame: A DataFrame containing all the collected data from different sources.
    """
    # Define the SQL query to fetch vehicle telematics data
    query = "SELECT * FROM vehicle_performance WHERE date >= '2023-01-01'"
    
    # Fetch data from SQL
    sql_data = fetch_data_from_sql(query)
    
    # Fetch data from CSV file
    csv_data = fetch_data_from_csv()
    
    # Merge the SQL and CSV data (if both exist)
    if not sql_data.empty and not csv_data.empty:
        merged_data = pd.concat([sql_data, csv_data], ignore_index=True)
        print("Data merged successfully from SQL and CSV.")
    else:
        # If one source is missing, fall back to the available data
        merged_data = sql_data if not sql_data.empty else csv_data
        print("Data collected from a single source due to missing data.")
    
    return merged_data

# Example usage of the function
if __name__ == "__main__":
    data = collect_data()
    if not data.empty:
        print(f"Collected Data:\n{data.head()}")
    else:
        print("No data collected.")
