import os
import pickle
import click
import mlflow
import mlflow.sklearn

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error

def load_pickle(filename: str):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)

@click.command()
@click.option(
    "--data_path",
    default="./output",
    help="Location where the processed NYC taxi trip data was saved"
)
def run_train(data_path: str):
    # Load datasets
    X_train, y_train = load_pickle(os.path.join(data_path, "train.pkl"))
    X_val, y_val = load_pickle(os.path.join(data_path, "val.pkl"))

    # Enable autologging
    mlflow.sklearn.autolog()

    with mlflow.start_run():
        # Train the model with the specified hyperparameters
        rf = RandomForestRegressor(max_depth=10, min_samples_split=2, random_state=0)
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_val)

        # Calculate RMSE
        rmse = root_mean_squared_error(y_val, y_pred)
        
        # Log the RMSE
        mlflow.log_metric("rmse", rmse)

        print(f'Validation RMSE: {rmse}')

if __name__ == '__main__':
    run_train()
