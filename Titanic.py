import streamlit as st
import pandas as pd
import numpy as np
import mlflow as ml
from sklearn.model_selection import train_test_split

st.title("Titanic Data Processing and Logging with MLflow")

# Load data
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
data = pd.read_csv(url)

# Data cleaning (handling missing Age values)
new_data = data.dropna(subset=['Age'])

# Display some data info in Streamlit
st.subheader("Data Overview")
st.write(f"Original data shape: {data.shape}")
st.write(f"Data shape after dropping NaN Age: {new_data.shape}")
st.write(f"Mean Age: {new_data['Age'].mean()}")
st.dataframe(new_data.head())  # Display the first few rows

# Split data
x = new_data.drop('Survived', axis=1)
y = new_data['Survived']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=42)

# MLflow setup and logging
esp = ml.set_experiment("Titanic")  # Or get existing experiment
with ml.start_run() as run:  # Use 'with' to ensure the run ends properly
    st.subheader("MLflow Logging")

    # Log parameters
    ml.log_param("mean_age", new_data["Age"].mean())
    ml.log_param("train_size", len(X_train))
    ml.log_param("test_size", len(X_test))
    ml.log_param("val_size", len(X_val))

    # Log metrics (You can add more relevant metrics later)
    # Example:  ml.log_metric("some_metric", 0.95)

    # Save data to CSV (in a temporary directory if needed for Streamlit sharing)
    X_train_path = "X_train.csv"  # Or use a tempfile if you don't want to save files
    X_test_path = "X_test.csv"
    X_val_path = "X_val.csv"
    titanic_path = "titanic.csv" #Path for the cleaned dataset

    new_data.to_csv(titanic_path, index=False)
    X_train.to_csv(X_train_path, index=False)
    X_test.to_csv(X_test_path, index=False)
    X_val.to_csv(X_val_path, index=False)


    # Log artifacts
    ml.log_artifact(titanic_path)
    ml.log_artifact(X_train_path)
    ml.log_artifact(X_test_path)
    ml.log_artifact(X_val_path)

    st.write(f"MLflow Run ID: {run.info.run_uuid}") #Display the run ID
    st.write("Data and parameters logged to MLflow.")

st.write("Done!")
