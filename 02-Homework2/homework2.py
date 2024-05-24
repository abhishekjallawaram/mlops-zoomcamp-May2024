import os
import subprocess
import sys

def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr)
        sys.exit(result.returncode)

def check_mlflow_version():
    print("Checking MLflow version...")
    # run_command([sys.executable, "-m", "pip", "install", "mlflow"]) ##already installed
    run_command(["mlflow", "--version"])

def preprocess_data():
    print("Running preprocessing...")
    run_command([sys.executable, "preprocess_data.py", "--raw_data_path", "../Data", "--dest_path", "output/"])

def train_model():
    print("Training model...")
    run_command([sys.executable, "train.py"])

def run_hpo():
    print("Running hyperparameter optimization...")
    run_command([sys.executable, "hpo.py"])

def register_best_model():
    print("Registering best model...")
    run_command([sys.executable, "register_model.py"])

def launch_tracking_server():
    print("Launching tracking server...")
    os.system("mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts")

def main():
    # Q1: Install MLflow and check version
    check_mlflow_version()

    # Q2: Download and preprocess the data
    preprocess_data()

    # Q3: Train a model with autolog
    train_model()

    # Q4: Launch the tracking server locally (This command needs to be run in a separate terminal or you can background it using &)
    print("Please run the following command in a separate terminal to keep the tracking server running:\n")
    print("mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts\n")

    # Q5: Tune model hyperparameters
    run_hpo()

    # Q6: Promote the best model to the model registry
    register_best_model()

if __name__ == "__main__":
    main()
