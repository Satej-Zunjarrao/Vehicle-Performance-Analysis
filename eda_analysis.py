# eda_analysis.py
# This script performs exploratory data analysis (EDA) on the vehicle performance data.
# It utilizes Matplotlib and Seaborn for visualizing key performance metrics and identifying patterns or anomalies.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Function to generate basic statistics for EDA
def generate_basic_statistics(data: pd.DataFrame):
    """
    Generates basic statistics like mean, median, and standard deviation for numerical columns.
    
    Parameters:
    data (pd.DataFrame): The cleaned data to generate statistics for.
    
    Returns:
    pd.DataFrame: A DataFrame containing basic statistics for numerical columns.
    """
    stats = data.describe()
    print("Basic statistics generated.")
    return stats

# Function to visualize fuel efficiency distribution
def plot_fuel_efficiency_distribution(data: pd.DataFrame):
    """
    Visualizes the distribution of fuel efficiency across the fleet.
    
    Parameters:
    data (pd.DataFrame): The cleaned data containing vehicle performance metrics.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data['fuel_efficiency'], kde=True, color='blue', bins=20)
    plt.title('Fuel Efficiency Distribution')
    plt.xlabel('Fuel Efficiency (mpg)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
    print("Fuel efficiency distribution plot displayed.")

# Function to visualize average speed vs engine load
def plot_speed_vs_engine_load(data: pd.DataFrame):
    """
    Visualizes the relationship between average speed and engine load.
    
    Parameters:
    data (pd.DataFrame): The cleaned data containing vehicle performance metrics.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='average_speed', y='engine_load', data=data, color='green')
    plt.title('Average Speed vs Engine Load')
    plt.xlabel('Average Speed (mph)')
    plt.ylabel('Engine Load (%)')
    plt.grid(True)
    plt.show()
    print("Average speed vs engine load scatter plot displayed.")

# Function to check correlation between numerical features
def plot_feature_correlation(data: pd.DataFrame):
    """
    Visualizes the correlation matrix for numerical features in the dataset.
    
    Parameters:
    data (pd.DataFrame): The cleaned data containing vehicle performance metrics.
    """
    correlation_matrix = data.corr()
    
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
    plt.title('Feature Correlation Matrix')
    plt.show()
    print("Feature correlation heatmap displayed.")

# Main function for performing EDA
def perform_eda():
    """
    Performs full exploratory data analysis (EDA) by generating basic statistics,
    visualizing key metrics, and checking feature correlations.
    
    Returns:
    pd.DataFrame: The cleaned data with added insights from EDA.
    """
    # Load the cleaned data
    data = load_cleaned_data(DATA_FILE_PATH)
    
    if not data.empty:
        # Generate basic statistics
        stats = generate_basic_statistics(data)
        print(f"Basic Statistics:\n{stats}\n")
        
        # Plot fuel efficiency distribution
        plot_fuel_efficiency_distribution(data)
        
        # Plot speed vs engine load
        plot_speed_vs_engine_load(data)
        
        # Plot feature correlation matrix
        plot_feature_correlation(data)
        
        print("Exploratory Data Analysis completed successfully.")
    else:
        print("No data available for EDA.")
    
    return data

# Example usage of the function
if __name__ == "__main__":
    eda_data = perform_eda()
    if not eda_data.empty:
        print(f"EDA completed on data:\n{eda_data.head()}")
    else:
        print("No data for EDA.")
