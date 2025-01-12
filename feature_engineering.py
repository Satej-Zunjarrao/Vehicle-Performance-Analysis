# feature_engineering.py
# This script performs feature engineering to derive new features from the raw vehicle performance data.
# The goal is to create metrics that will aid in predictive modeling, such as fuel efficiency per trip and idle time.

import pandas as pd

# Define the path to the cleaned data file (assuming it has been saved as 'cleaned_data.csv')
DATA_FILE_PATH = "C:/Users/Satej/Documents/Vehicle_Telematics/cleaned_data.csv"

# Function to load the cleaned data
def load_cleaned_data(file_path: str):
    """
    Loads the cleaned data from the specified CSV file into a Pandas DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file containing the cleaned data.
    
    Returns:
    pd.DataFrame: A Pandas DataFrame containing the cleaned data.
    """
    try:
        data = pd.read_csv(file_path)
        print("Cleaned data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading cleaned data from {file_path}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error

# Function to create fuel efficiency per trip
def create_fuel_efficiency_per_trip(data: pd.DataFrame):
    """
    Creates a new feature representing fuel efficiency per trip.
    Fuel efficiency per trip is calculated as distance traveled divided by fuel consumed.
    
    Parameters:
    data (pd.DataFrame): The cleaned data to create the feature from.
    
    Returns:
    pd.DataFrame: The data with the new fuel efficiency per trip feature added.
    """
    # Calculate fuel efficiency per trip (distance / fuel consumed)
    data['fuel_efficiency_per_trip'] = data['distance_traveled'] / data['fuel_consumed']
    print("Fuel efficiency per trip feature created.")
    return data

# Function to calculate idle time
def calculate_idle_time(data: pd.DataFrame):
    """
    Calculates the idle time for each vehicle. Idle time is assumed to be when speed is zero.
    
    Parameters:
    data (pd.DataFrame): The cleaned data to calculate idle time from.
    
    Returns:
    pd.DataFrame: The data with the idle time feature added.
    """
    # Assume idle time is when the vehicle speed is zero
    data['idle_time'] = data['average_speed'].apply(lambda x: 1 if x == 0 else 0)
    data['idle_time'] = data.groupby('vehicle_id')['idle_time'].transform('sum')
    print("Idle time feature created.")
    return data

# Function to create maintenance-critical metrics
def create_maintenance_critical_metrics(data: pd.DataFrame):
    """
    Creates maintenance-critical metrics such as engine load exceeding a threshold and high-speed driving.
    
    Parameters:
    data (pd.DataFrame): The cleaned data to create the feature from.
    
    Returns:
    pd.DataFrame: The data with the maintenance-critical features added.
    """
    # Flag high engine load (e.g., above 80%) as a critical metric
    data['high_engine_load'] = data['engine_load'].apply(lambda x: 1 if x > 80 else 0)
    
    # Flag high-speed driving (e.g., above 80 mph) as a critical metric
    data['high_speed_driving'] = data['average_speed'].apply(lambda x: 1 if x > 80 else 0)
    
    print("Maintenance-critical metrics created.")
    return data

# Main function to perform feature engineering
def engineer_features():
    """
    Performs feature engineering by adding new features like fuel efficiency per trip, idle time,
    and maintenance-critical metrics to the dataset.
    
    Returns:
    pd.DataFrame: The data with engineered features added.
    """
    # Load the cleaned data
    data = load_cleaned_data(DATA_FILE_PATH)
    
    if not data.empty:
        # Create fuel efficiency per trip
        data = create_fuel_efficiency_per_trip(data)
        
        # Calculate idle time
        data = calculate_idle_time(data)
        
        # Create maintenance-critical metrics
        data = create_maintenance_critical_metrics(data)
        
        print("Feature engineering completed successfully.")
    else:
        print("No data available for feature engineering.")
    
    return data

# Example usage of the function
if __name__ == "__main__":
    engineered_data = engineer_features()
    if not engineered_data.empty:
        print(f"Feature Engineering completed on data:\n{engineered_data.head()}")
    else:
        print("No engineered features available.")
