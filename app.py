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
def filter_by_location(df):
    location = input("Enter location: ")  # Prompt user to input location
    filtered_data = df[df['Location'] == location]  # Filter DataFrame by location

# Author: @Nicole
# Main function
def main():
    print("\n---------------------------------------------------")
    print("------------------- AGRI-LINK-1.0------------------")
    print("---------------------------------------------------")
    while True:
        print("\n\n[bold blue]Select your role:[/bold blue]")
        print("1. Agency")
        print("2. Farmer")
        print("3. Exit")
        choice = input("\nEnter your choice (1, 2, or 3): ")  # Prompt user to select choice

    if choice == '1':  # If choice is 1 (Agency)
                args = argparse.Namespace(role='agency')  # Simulate argparse Namespace for agency
                data = input_climate_data()  # Input climate data
                save_to_csv([data])  # Save climate data to CSV file
                print("[bold green]Climate data saved successfully.[/bold green]")  # Print success message
    elif choice == '2':  # If choice is 2 (Farmer)
                args = argparse.Namespace(role='farmer')  # Simulate argparse Namespace for farmer
                display_options_farmers()  # Display options for farmers
                option = input("Enter your choice (1, 2, or 3): ")  # Prompt user to select option
                df = load_from_csv()  # Load climate data from CSV file
                if option == '1':  # If option is 1 (List all data)
                    if df.empty:
                        print("[bold red]No climate data available.[/bold red]")  # Print message if no data found
                    else:
                        display_data(df)  # Display all data
                elif option == '2':  # If option is 2 (Search by date)
                    filter_by_date(df)  # Filter data by date
                elif option == '3':  # If option is 3 (Search by location)
                    filter_by_location(df)  # Filter data by location
                else:
                    print("[bold red]Invalid choice. Please enter 1, 2, or 3.[/bold red]")  # Print error message for invalid choice
    elif choice == '3':

                print("[bold]Exiting...[/bold]")
                break
    else:
        print("[bold red]Invalid choice. Please enter 1, 2, or 3.[/bold red]")