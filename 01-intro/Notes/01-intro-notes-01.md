# ML Zoomcamp Repository

This repository is for setting up and working through the ML Zoomcamp course using GitHub Codespaces.

- [ML Zoomcamp Repository](#ml-zoomcamp-repository)
  - [Introduction](#introduction)
  - [Prerequisites](#prerequisites)
  - [Steps to Set Up](#steps-to-set-up)
    - [1. Create a New Repository](#1-create-a-new-repository)
    - [2. Set Up GitHub Codespaces](#2-set-up-github-codespaces)
    - [3. Configure Codespace](#3-configure-codespace)
    - [4. Managing Codespaces](#4-managing-codespaces)
    - [5. Additional Notes](#5-additional-notes)
    - [6. Pricing](#6-pricing)


## Introduction

This guide provides instructions on configuring your environment using GitHub Codespaces. This setup is an alternative to the traditional local setup and is simpler and quicker.

## Prerequisites

- GitHub account
- Access to GitHub Codespaces

## Steps to Set Up

### 1. Create a New Repository

1. Go to GitHub and create a new repository named `ml-zoomcamp`.
2. Add a README file and a .gitignore template for Python.
3. Ensure the repository is public.

### 2. Set Up GitHub Codespaces

1. Navigate to your repository.
2. Click on the `Code` button, select the `Codespaces` tab, and create a new Codespace on `main`.

### 3. Configure Codespace

1. Open the terminal in Codespaces.
2. Install Docker (already pre-installed in Codespaces):
   ```sh
   docker run hello-world
    ```
3. Open the Codespace in Visual Studio Code desktop for better performance and port forwarding capabilities.
4. Install Anaconda
   1. Download and install Anaconda:
   ```sh
    wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh
    bash Anaconda3-2021.05-Linux-x86_64.sh
    ```
   2. Follow the prompts to complete the installation and initialize Anaconda.
5. Create Project Structure
   1. Create a directory for the intro module:
   ```sh
    mkdir -p 01-intro
    cd 01-intro
    ```
6. Run Jupyter Notebook
   1. Start Jupyter Notebook:
   ```sh
   jupyter notebook
    ```
   2. Forward the port in Codespaces and open Jupyter in your browser.
7. Example Workflow
   1. Create a new Jupyter notebook named `First-Notebook-Test`.
   2. Install required packages directly from the notebook:
   ```sh
   !pip install pandas pyarrow    
   ```
   3. Load and process data:
   ```sh
    import pandas as pd
    df = pd.read_parquet("URL_TO_PARQUET_FILE")
   ```
8. Commit and Push Changes
   1. Commit your changes:
   ```python
        git add .
        git commit -m "Initial setup and first commit"
        git push origin main
    ```

### 4. Managing Codespaces

1. To stop the Codespace, go to the Codespaces tab in GitHub and click "Stop".
2. To delete a Codespace, select the Codespace and click "Delete". This will remove all data, including Anaconda and configurations.

### 5. Additional Notes

1. Ensure you have the GitHub Codespaces extension installed in Visual Studio Code.
2. Configure AWS or other services as needed for subsequent modules.

### 6. Pricing

GitHub Codespaces offers free usage up to a certain limit, with additional usage requiring payment. Refer to GitHub Codespaces Pricing for more details.
