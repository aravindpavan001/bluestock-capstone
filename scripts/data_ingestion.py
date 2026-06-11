"""
ETL script for loading and transforming mutual fund data.

Author: Repalle Aravind Pavan Kumar
Project: Bluestock Mutual Fund Capstone
"""
import pandas as pd
import os

folder_path = "data/raw"

files = os.listdir(folder_path)

for file in files:
    if file.endswith(".csv"):

        path = os.path.join(folder_path, file)

        print("\n" + "="*50)
        print(f"DATASET: {file}")
        print("="*50)

        df = pd.read_csv(path)

        print("\nShape:")
        print(df.shape)

        print("\nColumns and Data Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("\nFirst 5 Rows:")
        print(df.head())