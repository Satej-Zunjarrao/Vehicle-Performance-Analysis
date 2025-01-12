# automation_pipeline.py
# This script builds an automated pipeline for continuously ingesting, processing, and updating vehicle performance data.
# The pipeline ensures the dashboard is up-to-date and ready for real-time decision-making.

import pandas as pd
import os
import time
from data_collection import collect_data
from data_cleaning import clean_data
from feature_engineering import engineer_features
from predictive_modeling import predictive_modeling

# Define paths for the processed data and model
PROCESSED_DATA_PATH = "C:/Users/Satej/Documents/Vehicle_Telematics/processed_data.csv"
MODEL_PATH = "C:/Users/Satej/Documents/Vehicle_Telematics/model.pkl"

# Function to check if new data is available
def check_for_new_data():
    """
    Checks if new data files are available by monitoring the data directory.
    
    Returns:
    bool: True if new data is available, False otherwise.
    """
    # For simplicity, we check if the 'vehicle_data.db' file has been updated (you can modify this logic as needed)
    data_directory = "C:/Users/Satej/Documents/Vehicle_Telematics/"
    file_timestamp = os.path.getmtime(data_directory + "vehicle_data.db")
    
    current_time = time.time()
    if current_time - file_timestamp < 86400:  # 1 day in seconds (you can modify this threshold)
        return True
    return False

# Function to automate the entire pipeline
def automate_pipeline():
    """
    Automates the data ingestion, cleaning, feature engineering, and model prediction pipeline.
    Ensures that the processed data and predictive model are up-to-date.
    """
    if check_for_new_data():
        print("New data available. Starting pipeline...")
        
        # Step 1: Data Collection
        collected_data = collect_data()
        if not collected_data.empty:
            collected_data.to_csv(PROCESSED_DATA_PATH, index=False)
            print("Data collection completed and saved.")
        
        # Step 2: Data Cleaning
        cleaned_data = clean_data()
        if not cleaned_data.empty:
            cleaned_data.to_csv(PROCESSED_DATA_PATH, index=False)
            print("Data cleaning completed and saved.")
        
        # Step 3: Feature Engineering
        engineered_data = engineer_features()
        if not engineered_data.empty:
            engineered_data.to_csv(PROCESSED_DATA_PATH, index=False)
            print("Feature engineering completed and saved.")
        
        # Step 4: Predictive Modeling
        model = predictive_modeling()
        print("Model trained and evaluated successfully.")
        
        # Save the model for later use
        import joblib
        joblib.dump(model, MODEL_PATH)
        print(f"Model saved to {MODEL_PATH}")
        
    else:
        print("No new data available. Skipping pipeline.")

# Main function to run the automation pipeline
def main():
    """
    Runs the entire automation pipeline.
    """
    while True:
        automate_pipeline()
        time.sleep(3600)  # Check for new data every hour (can adjust as needed)

# Example usage of the function
if __name__ == "__main__":
    main()
