import pandas as pd
import numpy as np
import mlflow as ml
from sklearn.model_selection import train_test_split

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
data = pd.read_csv(url)

new_data = data.dropna(subset=['Age'])

new_data.to_csv('titanic.csv', index=False)

x = new_data.drop('Survived', axis=1)
y = new_data['Survived']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=42)

esp = ml.set_experiment("Titanic")
with ml.start_run():
    # Log các tham số (parameters)
    # mlflow.log_param("Age", 25)
    # mlflow.log_param("Sex", "male")
    ml.log_param("mean_age", new_data["Age"].mean())

    # Log các số liệu (metrics)
    # mlflow.log_metric("accuracy", 0.85)
    # mlflow.log_metric("loss", 0.2)
    ml.log_metric("train_size", len(X_train))
    ml.log_metric("test_size", len(X_test))
    ml.log_metric("val_size", len(X_val))

    # Log các artifact (ví dụ: mô hình, file dữ liệu)
    ml.log_artifact("titanic.csv")  # Thay thế bằng đường dẫn đến artifact của bạn
