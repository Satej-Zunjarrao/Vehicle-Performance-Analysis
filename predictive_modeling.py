# predictive_modeling.py
# This script is responsible for building a machine learning model to predict maintenance needs of vehicles.
# The model is trained using historical performance data, operating conditions, and maintenance history.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

# Define the path to the feature-engineered data file (assuming it has been saved as 'engineered_data.csv')
DATA_FILE_PATH = "C:/Users/Satej/Documents/Vehicle_Telematics/engineered_data.csv"

# Function to load the engineered data
def load_engineered_data(file_path: str):
    """
    Loads the feature-engineered data from the specified CSV file into a Pandas DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file containing the engineered data.
    
    Returns:
    pd.DataFrame: A Pandas DataFrame containing the engineered data.
    """
    try:
        data = pd.read_csv(file_path)
        print("Engineered data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading engineered data from {file_path}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error

# Function to split the data into features and target
def split_data(data: pd.DataFrame):
    """
    Splits the dataset into features (X) and target (y) for predictive modeling.
    
    Parameters:
    data (pd.DataFrame): The dataset containing the features and target.
    
    Returns:
    X (pd.DataFrame): Features for training the model.
    y (pd.Series): Target variable for the model.
    """
    # Assume 'maintenance_required' is the target variable to predict
    X = data.drop(columns=['maintenance_required', 'vehicle_id'])
    y = data['maintenance_required']
    print("Data split into features and target.")
    return X, y

# Function to preprocess the data (scaling)
def preprocess_data(X: pd.DataFrame):
    """
    Standardizes the features to have zero mean and unit variance using StandardScaler.
    
    Parameters:
    X (pd.DataFrame): The features to scale.
    
    Returns:
    X_scaled (pd.DataFrame): The scaled features.
    """
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print("Features scaled successfully.")
    return X_scaled

# Function to train the machine learning model
def train_model(X_train: pd.DataFrame, y_train: pd.Series):
    """
    Trains a Random Forest Classifier model on the training data.
    
    Parameters:
    X_train (pd.DataFrame): The training features.
    y_train (pd.Series): The training target variable.
    
    Returns:
    model (RandomForestClassifier): The trained Random Forest model.
    """
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print("Model trained successfully.")
    return model

# Function to evaluate the model
def evaluate_model(model, X_test: pd.DataFrame, y_test: pd.Series):
    """
    Evaluates the trained model using the test data and prints classification metrics.
    
    Parameters:
    model (RandomForestClassifier): The trained model.
    X_test (pd.DataFrame): The test features.
    y_test (pd.Series): The true labels for the test set.
    """
    y_pred = model.predict(X_test)
    print("Model evaluation completed.")
    
    # Classification report and confusion matrix
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

# Main function to train and evaluate the predictive model
def predictive_modeling():
    """
    Loads the engineered data, splits it into features and target, preprocesses the data,
    trains a Random Forest model, and evaluates its performance.
    
    Returns:
    model (RandomForestClassifier): The trained machine learning model.
    """
    # Load the engineered data
    data = load_engineered_data(DATA_FILE_PATH)
    
    if not data.empty:
        # Split the data into features and target
        X, y = split_data(data)
        
        # Split the data into training and testing sets (80% train, 20% test)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Preprocess the data (standardization)
        X_train_scaled = preprocess_data(X_train)
        X_test_scaled = preprocess_data(X_test)
        
        # Train the model
        model = train_model(X_train_scaled, y_train)
        
        # Evaluate the model
        evaluate_model(model, X_test_scaled, y_test)
    else:
        print("No data available for modeling.")
    
    return model

# Example usage of the function
if __name__ == "__main__":
    model = predictive_modeling()
