# Fossil Fuel CO2 Emission Visualization Dashboard

![Fossil Fuel Emission Dashboard](https://github.com/Ragzz258/fossil-fuel-emission-dashboard/blob/main/sample_img.jpg)


## Introduction

This dashboard is designed to visualize fossil fuel CO2 emissions of a particular country on a world map. Users can select a specific year from the dropdown menu, and the map will display the emissions data for that year. This project uses Python, Plotly, and Dash for data visualization and interactivity.

## Features

- Interactive dropdown menu to select the desired year.
- Choropleth map visualization showing fossil fuel CO2 emissions by country.
- Clear display of the selected year.
- Data sourced from a CSV file.

## Installation

To run this project on your local machine, follow these steps:

1. Clone the repository:
```
git clone https://github.com/Ragzz258/fossil-fuel-emission-dashboard.git
```
2. Navigate to the project directory:
```
cd fossil-fuel-emission-dashboard/
```

3. Install the required Python libraries:
```
pip install pandas
pip install plotly
pip install dash
```
4. Run the Dash app:
```
python3 app.py
```

## Data Source

The emissions data is sourced from the "fossil-fuel-co2-emissions-by-nation.csv" file, which should be placed in the same directory as your app script.

## Usage

1. Launch the app using the steps mentioned in the "Installation" section.

2. Once the app is running, open a web browser and navigate to the provided local server address.

3. Select a year from the dropdown menu to view fossil fuel CO2 emissions for that year.

4. The map will update to display emissions data by country.
