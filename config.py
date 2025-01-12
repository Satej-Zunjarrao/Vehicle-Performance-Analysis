# config.py
# This file contains configuration settings that are used across the project.
# It includes paths, database credentials, and other necessary configurations.

import os

# Paths to data files and directories
BASE_PATH = "C:/Users/Satej/Documents/Vehicle_Telematics/"
SQL_DATABASE_PATH = os.path.join(BASE_PATH, "vehicle_data.db")
CSV_FILE_PATH = os.path.join(BASE_PATH, "vehicle_performance_data.csv")
PROCESSED_DATA_PATH = os.path.join(BASE_PATH, "processed_data.csv")
EXPORT_FILE_PATH = os.path.join(BASE_PATH, "dashboard_export.csv")
MODEL_PATH = os.path.join(BASE_PATH, "model.pkl")

# Database connection details (example with SQLite, you can adjust this for your database type)
DB_HOST = "localhost"  # For SQLite, this can be a file path; for MySQL/Postgres, this would be an IP or domain
DB_PORT = "5432"  # Default port for PostgreSQL (change if using another DB)
DB_NAME = "vehicle_telematics"
DB_USER = "satej"
DB_PASSWORD = "yourpassword"  # Replace with your actual password (can be loaded from an environment variable for security)

# Time settings (for automation pipeline frequency, etc.)
CHECK_NEW_DATA_INTERVAL = 3600  # Check for new data every hour (in seconds)
DATA_UPDATE_THRESHOLD = 86400  # 1 day (in seconds), check if data is updated within the last 24 hours

# Model settings
RANDOM_FOREST_N_ESTIMATORS = 100  # Number of trees in Random Forest

# Logging settings (you can change these to integrate with a logging library if needed)
LOGGING_ENABLED = True
LOG_FILE_PATH = os.path.join(BASE_PATH, "logs/project_log.txt")

# Function to print configurations for testing or debugging purposes
def print_config():
    print("Configuration Settings:")
    print(f"BASE_PATH: {BASE_PATH}")
    print(f"SQL_DATABASE_PATH: {SQL_DATABASE_PATH}")
    print(f"CSV_FILE_PATH: {CSV_FILE_PATH}")
    print(f"PROCESSED_DATA_PATH: {PROCESSED_DATA_PATH}")
    print(f"EXPORT_FILE_PATH: {EXPORT_FILE_PATH}")
    print(f"MODEL_PATH: {MODEL_PATH}")
    print(f"DB_HOST: {DB_HOST}")
    print(f"DB_PORT: {DB_PORT}")
    print(f"DB_NAME: {DB_NAME}")
    print(f"DB_USER: {DB_USER}")
    print(f"CHECK_NEW_DATA_INTERVAL: {CHECK_NEW_DATA_INTERVAL}")
    print(f"DATA_UPDATE_THRESHOLD: {DATA_UPDATE_THRESHOLD}")

# Example usage of configuration print function
if __name__ == "__main__":
    print_config()
