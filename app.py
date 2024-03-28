# Author: @Patrick
import argparse  # Module for parsing command-line arguments
import pandas as pd  # Module for data manipulation and analysis
from rich import print  # Import rich print for styled printing
from rich.console import Console  # Import rich console for styled output
from rich.table import Table  # Import rich table for styled tables
import os  # Module providing functions to interact with the operating system

# Initialize rich console
console = Console()

# Function to save climate data to a CSV file
def save_to_csv(data):
    df = pd.DataFrame(data)  # Create DataFrame from input data
    df.to_csv('climate_data.csv', mode='a', index=False, header=not os.path.exists('climate_data.csv'))  # Save DataFrame to CSV file

# Function to load climate data from a CSV file
def load_from_csv():
    try:
        df = pd.read_csv('climate_data.csv')  # Read data from CSV file into DataFrame
        return df
    except FileNotFoundError:
        return pd.DataFrame()  # Return empty DataFrame if file is not found