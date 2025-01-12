# Vehicle Performance Analysis

Built an analytics system to monitor vehicle performance, optimize fuel consumption, predict maintenance needs, and provide insights to improve fleet efficiency.

# Vehicle Performance Monitoring System

## Overview
The **Vehicle Performance Monitoring System** is a Python-based solution designed to analyze telematics data from vehicles. This system aims to optimize fuel consumption, predict maintenance needs, and offer actionable insights for improving overall fleet efficiency. It uses advanced data wrangling, predictive analytics, and machine learning models to make data-driven decisions that enhance fleet operations.

This project includes a modular pipeline for data collection, cleaning, exploratory analysis, feature engineering, predictive modeling, and automation.

---

## Key Features
- **Data Collection**: Ingests telematics data from SQL databases and flat files.
- **Data Cleaning**: Preprocesses and cleans raw data by handling missing values, outliers, and data inconsistencies.
- **Exploratory Data Analysis (EDA)**: Visualizes key metrics like fuel efficiency, speed, and engine load to derive insights.
- **Feature Engineering**: Derives advanced features such as fuel efficiency per trip, idle time, and maintenance-critical metrics.
- **Predictive Modeling**: Builds machine learning models (Random Forest) to predict maintenance needs and optimize fleet operations.
- **Automation**: Automates the pipeline to process and update vehicle data periodically.
- **Visualization**: Exports processed data for integration with Tableau or other visualization tools to generate real-time fleet performance dashboards.

---

## Directory Structure
```
project/
│
├── data_collection.py          # Handles data ingestion from SQL databases and flat files
├── data_cleaning.py            # Preprocesses and cleans raw vehicle telematics data
├── eda_analysis.py             # Performs exploratory data analysis and visualizations
├── feature_engineering.py      # Creates new features from raw data for model training
├── predictive_modeling.py      # Builds and evaluates machine learning models for predictive analytics
├── automation_pipeline.py      # Automates data processing and model updating
├── dashboard_export.py         # Exports processed data for Tableau or other visualization tools
├── config.py                   # Stores reusable configurations like file paths and database credentials
├── utils.py                    # Helper functions for logging, metrics, and task scheduling
├── README.md                   # Project documentation
```


# Modules

## 1. data_collection.py
- Ingests data from SQL databases and flat files (CSV format).
- Handles database connections, queries, and data fetching.

## 2. data_cleaning.py
- Preprocesses the raw telematics data, handling missing values, outliers, and data inconsistencies.
- Outputs a cleaned dataset ready for analysis and modeling.

## 3. eda_analysis.py
- Performs exploratory data analysis to visualize key metrics such as fuel efficiency, speed, and engine load.
- Identifies patterns, trends, and anomalies in the vehicle performance data.

## 4. feature_engineering.py
- Creates advanced features such as fuel efficiency per trip, idle time, and maintenance-critical metrics.
- Outputs a dataset with the newly engineered features.

## 5. predictive_modeling.py
- Builds machine learning models (Random Forest) to predict maintenance needs and optimize fleet performance.
- Trains and evaluates models using historical performance data and maintenance history.

## 6. automation_pipeline.py
- Automates the data collection, cleaning, feature engineering, and model training pipeline.
- Periodically processes new data and updates the model using scheduled tasks.

## 7. dashboard_export.py
- Exports processed data to CSV format for integration with Tableau or other visualization tools.
- Prepares the data for creating real-time dashboards and reporting.

## 8. config.py
- Centralized configuration file containing paths to data files, database credentials, and model settings.

## 9. utils.py
- Provides helper functions for logging, task scheduling, and other utility tasks such as random seed initialization.

# Contact

For queries or collaboration, feel free to reach out:

- **Name**: Satej Zunjarrao  
- **Email**: zsatej1028@gmail.com
