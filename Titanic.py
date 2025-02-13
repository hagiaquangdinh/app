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


st.write(f"MLflow Run ID: {run.info.run_uuid}") #Display the run ID
st.write("Data and parameters logged to MLflow.")

st.write("Done!")
