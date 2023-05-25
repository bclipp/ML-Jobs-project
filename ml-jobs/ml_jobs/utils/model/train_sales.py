"""
fill me in
"""
import mlflow
import numpy as np
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor


def train_sales(model_data, experiment, model_path):
    """
    fill me in
    """

    max_depth = 2
    n_estimators = 100
    with mlflow.start_run(experiment_id=experiment):
        rf = RandomForestRegressor(
            max_depth=max_depth, n_estimators=n_estimators, random_state=0
        )
        rf.fit(model_data["X_train"], model_data["y_train"])
        y_pred = rf.predict(model_data["X_test"])
        rmse = np.sqrt(
            metrics.mean_squared_error(model_data["y_test"], model_data["y_pred"])
        )
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_metric("rmse", rmse)
        mlflow.sklearn.log_model(rf, "model")
        mlflow.sklearn.save_model(rf, model_path)
