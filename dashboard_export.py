# dashboard_export.py
# This script exports the processed data to Tableau or any other visualization tool for creating a dashboard.
# It ensures that the data is in the correct format for use in the dashboard and updates it periodically.

import pandas as pd

# Define the path to the processed data file (assuming it has been saved as 'processed_data.csv')
PROCESSED_DATA_PATH = "C:/Users/Satej/Documents/Vehicle_Telematics/processed_data.csv"
# Define the path for the dashboard export
EXPORT_FILE_PATH = "C:/Users/Satej/Documents/Vehicle_Telematics/dashboard_export.csv"

# Function to load the processed data
def load_processed_data(file_path: str):
    """
    Loads the processed data from the specified CSV file into a Pandas DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file containing the processed data.
    
    Returns:
    pd.DataFrame: A Pandas DataFrame containing the processed data.
    """
    try:
        data = pd.read_csv(file_path)
        print("Processed data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading processed data from {file_path}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error

# Function to prepare the data for export (e.g., selecting relevant columns or aggregating data)
def prepare_data_for_export(data: pd.DataFrame):
    """
    Prepares the data for export by selecting relevant columns and performing any necessary transformations.
    
    Parameters:
    data (pd.DataFrame): The processed data to prepare for export.
    
    Returns:
    pd.DataFrame: The prepared data ready for export.
    """
    # Select relevant columns for the dashboard
    columns_to_export = ['vehicle_id', 'fuel_efficiency', 'maintenance_required', 'average_speed', 'engine_load', 'idle_time']
    
    # Filter the data to include only the relevant columns
    export_data = data[columns_to_export]
    
    # Example: Aggregating data by vehicle_id if needed
    export_data = export_data.groupby('vehicle_id').agg({
        'fuel_efficiency': 'mean',
        'maintenance_required': 'sum',
        'average_speed': 'mean',
        'engine_load': 'mean',
        'idle_time': 'sum'
    }).reset_index()
    
    print("Data prepared for export.")
    return export_data

# Function to export the data to a CSV file (for Tableau or other tools)
def export_to_csv(data: pd.DataFrame, file_path: str):
    """
    Exports the prepared data to a CSV file for use in Tableau or other visualization tools.
    
    Parameters:
    data (pd.DataFrame): The data to be exported.
    file_path (str): The path where the data should be saved as a CSV file.
    """
    try:
        data.to_csv(file_path, index=False)
        print(f"Data successfully exported to {file_path}.")
    except Exception as e:
        print(f"Error exporting data to CSV: {e}")

# Main function to load, prepare, and export data for the dashboard
def export_dashboard_data():
    """
    Loads the processed data, prepares it for export, and then exports it to a CSV file for use in a dashboard.
    """
    # Load the processed data
    data = load_processed_data(PROCESSED_DATA_PATH)
    
    if not data.empty:
        # Prepare the data for export
        prepared_data = prepare_data_for_export(data)
        
        # Export the prepared data to a CSV file
        export_to_csv(prepared_data, EXPORT_FILE_PATH)
    else:
        print("No data available to export.")

# Example usage of the function
if __name__ == "__main__":
    export_dashboard_data()
