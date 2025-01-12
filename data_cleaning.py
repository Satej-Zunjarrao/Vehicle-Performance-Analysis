# data_cleaning.py
# This script is designed to clean and preprocess the raw vehicle performance data.
# The goal is to handle missing values, remove outliers, and standardize the data for analysis.

import pandas as pd
import numpy as np

# Define the path to the collected data file (assuming it has been saved as 'merged_data.csv')
DATA_FILE_PATH = "C:/Users/Satej/Documents/Vehicle_Telematics/merged_data.csv"

# Function to load the collected data from a CSV file
def load_data(file_path: str):
    """
    Loads the collected data from the specified CSV file into a Pandas DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file containing the collected data.
    
    Returns:
    pd.DataFrame: A Pandas DataFrame containing the raw data.
    """
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error

# Function to handle missing values by imputing or removing rows
def handle_missing_values(data: pd.DataFrame):
    """
    Handles missing values in the dataset by either imputing or dropping rows based on the column importance.
    
    Parameters:
    data (pd.DataFrame): The raw data that needs to be cleaned.
    
    Returns:
    pd.DataFrame: The cleaned data with missing values handled.
    """
    # Impute missing values in numerical columns with the median
    numeric_columns = data.select_dtypes(include=[np.number]).columns
    for col in numeric_columns:
        median_value = data[col].median()
        data[col].fillna(median_value, inplace=True)
        print(f"Missing values in {col} replaced with median value: {median_value}")
    
    # Drop rows with missing values in categorical columns (if any)
    categorical_columns = data.select_dtypes(include=[object]).columns
    data.dropna(subset=categorical_columns, inplace=True)
    print("Rows with missing values in categorical columns have been dropped.")
    
    return data

# Function to remove outliers using the Z-score method
def remove_outliers(data: pd.DataFrame, threshold: float = 3.0):
    """
    Removes outliers in the dataset by using the Z-score method. Any data point with a Z-score greater than
    the specified threshold is considered an outlier and is removed.
    
    Parameters:
    data (pd.DataFrame): The cleaned data from which outliers need to be removed.
    threshold (float): The Z-score threshold above which data points will be considered outliers.
    
    Returns:
    pd.DataFrame: The data with outliers removed.
    """
    # Calculate Z-scores for the numeric columns
    numeric_columns = data.select_dtypes(include=[np.number]).columns
    z_scores = np.abs((data[numeric_columns] - data[numeric_columns].mean()) / data[numeric_columns].std())
    
    # Identify rows where any Z-score exceeds the threshold
    data_no_outliers = data[(z_scores < threshold).all(axis=1)]
    print(f"Removed outliers based on Z-score threshold of {threshold}.")
    
    return data_no_outliers

# Function to standardize the data (optional, for further analysis)
def standardize_data(data: pd.DataFrame):
    """
    Standardizes the data by scaling numerical features to have zero mean and unit variance.
    
    Parameters:
    data (pd.DataFrame): The cleaned data to be standardized.
    
    Returns:
    pd.DataFrame: The standardized data.
    """
    numeric_columns = data.select_dtypes(include=[np.number]).columns
    data[numeric_columns] = (data[numeric_columns] - data[numeric_columns].mean()) / data[numeric_columns].std()
    print("Data has been standardized.")
    return data

# Main function to clean the data
def clean_data():
    """
    The main function to load, clean, and preprocess the data. This involves handling missing values,
    removing outliers, and standardizing the data.
    
    Returns:
    pd.DataFrame: The fully cleaned and preprocessed data ready for analysis.
    """
    # Load the collected data
    data = load_data(DATA_FILE_PATH)
    
    if not data.empty:
        # Handle missing values
        data = handle_missing_values(data)
        
        # Remove outliers
        data = remove_outliers(data)
        
        # Optionally, standardize the data
        data = standardize_data(data)
        
        print("Data cleaning process completed successfully.")
    else:
        print("No data to clean.")
    
    return data

# Example usage of the function
if __name__ == "__main__":
    cleaned_data = clean_data()
    if not cleaned_data.empty:
        print(f"Cleaned Data:\n{cleaned_data.head()}")
    else:
        print("No cleaned data available.")
