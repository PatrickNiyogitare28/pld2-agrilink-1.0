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


# Author @Blessing
# Function to display data in a formatted table
def display_data(df):
    if df.empty:
        print("[bold red]No data available.[/bold red]")  # Print message if DataFrame is empty
    else:
        table = Table(show_header=True, header_style="bold magenta")  # Create a table for displaying data
        table.add_column("Date", style="cyan", justify="center")  # Add column for Date
        table.add_column("Location", style="cyan", justify="center")  # Add column for Location
        table.add_column("Temperature", style="cyan", justify="center")  # Add column for Temperature
        table.add_column("Precipitation", style="cyan", justify="center")  # Add column for Precipitation
        table.add_column("Humidity", style="cyan", justify="center")  # Add column for Humidity
        table.add_column("Wind Speed", style="cyan", justify="center")  # Add column for Wind Speed

        # Add rows for each data entry
        for index, row in df.iterrows():
            table.add_row(
                str(row['Date']),
                str(row['Location']),
                str(row['Temperature']),
                str(row['Precipitation']),
                str(row['Humidity']),
                str(row['Wind Speed'])
            )

        console.print(table)  # Print the table to console
# Author @izerekerie
# Function to filter data by date
def filter_by_date(df):
    date = input("Enter date (YYYY-MM-DD): ")  # Prompt user to input date
    filtered_data = df[df['Date'] == date]  # Filter DataFrame by date
    if filtered_data.empty:
        print("No data available for the given date.")  # Print message if no data found
    else:
        display_data(filtered_data)  # Display filtered data