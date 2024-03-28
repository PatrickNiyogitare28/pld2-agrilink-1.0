# Agri-Link 1.0

Agri-Link 1.0 is a command-line application designed to assist both climate agency personnel and local farmers in accessing and managing climate data for specific locations across sub-Saharan Africa.

## Features
- Climate agency personnel can input climate metrics (temperature, precipitation, humidity, wind speed) for specific dates and locations, which are then saved into a CSV file.
- Farmers can access climate data for specific locations, view it in visually appealing formats, and filter it by date or location.

## Libraries Used
- [pandas](https://pandas.pydata.org/): Used for data manipulation and analysis.
- [rich](https://rich.readthedocs.io/en/latest/): Used for styling and formatting output in the terminal.

## How to Run
1. Make sure you have Python installed on your system.
2. Install the required libraries by running: `pip install pandas rich`.
3. Download or clone this repository to your local machine.
4. Navigate to the directory containing the files.
5. Run the program by executing `python app.py` in your terminal.
6. Follow the on-screen instructions to interact with the program.

## Usage
- Select your role: Agency or Farmer.
- For agency personnel:
  - Input climate metrics when prompted.
- For farmers:
  - Choose from options to list all data, search by date, or search by location.
  - Follow the prompts to input date or location for filtering data.

## Example