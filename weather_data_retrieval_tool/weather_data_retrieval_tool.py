# Weather Data Retrieval Tool

# Step 1: Importing required libraries
import requests  # For making HTTP requests
import csv  # For saving data to CSV files
import os  # For handling file paths and directories
from datetime import datetime  # For validating date input

# Step 2: Function to validate date input
def validate_date(date_text):
    """
    Validate that the input is in the correct 'YYYY-MM-DD' format.

    Parameters:
        date_text (str): Input date as a string.

    Returns:
        bool: True if valid, False otherwise.
    """
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False


# Step 3: Function to get coordinates of a city using OpenCage API
def get_coordinates(city_name, state_name="", country_name=""):
    """
    Retrieve latitude and longitude for a city using the OpenCage API.

    Parameters:
        city_name (str): Name of the city.
        state_name (str): Name of the state (optional).
        country_name (str): Name of the country (optional).

    Returns:
        tuple: Latitude and longitude of the location.
    """
    # Constructing the query with city, state, and country
    query = f"{city_name}"
    if state_name:
        query += f", {state_name}"
    if country_name:
        query += f", {country_name}"

    # OpenCage Geocoder API URL
    api_key = "your_opencage_api_key"  # Replace with your actual API key
    geocoding_url = f"https://api.opencagedata.com/geocode/v1/json?q={query}&key={api_key}"

    # Masked URL for display
    masked_api_key = "****"
    masked_url = geocoding_url.replace(api_key, masked_api_key)

    print("Retrieving coordinates...")
    print(f"Generated API URL: {masked_url}")  # Print the masked URL

    try:
        # Sending a GET request to the geocoding API
        response = requests.get(geocoding_url, timeout=10)
        response.raise_for_status()  # Check if the HTTP request was successful
        json_response = response.json()  # Parse the JSON response

        # Check if the response contains results
        if json_response['results']:
            selected_location = json_response['results'][0]  # Select the first result
            print(f"Found Location: {selected_location['formatted']}")
            return (
                selected_location['geometry']['lat'],  # Latitude
                selected_location['geometry']['lng']   # Longitude
            )
        else:
            # Handle cases where no results are found
            raise ValueError(f"No results found for '{query}'. Please refine your input.")
    except requests.exceptions.RequestException as e:
        # Handle request errors
        print(f"Error while making API request: {e}")
        raise
    except ValueError as ve:
        # Handle cases of invalid input or no results
        print(ve)
        raise


# Step 4: Function to fetch weather data and save it to a CSV file
def fetch_weather_data(lat, lon, start_date, end_date, city_name, output_folder):
    """
    Fetch historical weather data using the Open-Meteo API and save it to a CSV file.

    Parameters:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.
        city_name (str): Name of the city for the output file name.
        output_folder (str): Path where the output file will be saved.
    """
    print(f"Fetching weather data for {city_name}...")
    weather_url = (
        f"https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}"
        f"&start_date={start_date}&end_date={end_date}"
        f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,windspeed_10m_max"
        f"&timezone=auto"
    )

    try:
        response = requests.get(weather_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        daily_data = data['daily']

        # Ensure the output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # Prepare the full file path
        output_file = os.path.join(output_folder, f"{city_name.replace(' ', '_')}_weather_data.csv")
        print(f"Saving file to: {output_file}")  # Debugging file path

        # Save data to CSV file
        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Max Temp (°C)', 'Min Temp (°C)', 'Precipitation (mm)', 'Max Wind Speed (km/h)'])

            for i in range(len(daily_data['time'])):
                writer.writerow([
                    daily_data['time'][i],
                    daily_data['temperature_2m_max'][i],
                    daily_data['temperature_2m_min'][i],
                    daily_data['precipitation_sum'][i],
                    daily_data['windspeed_10m_max'][i]
                ])
        print(f"Weather data has been saved to {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"Error while fetching weather data: {e}")
    except KeyError:
        print("Unexpected response format. Please check the API or try again later.")
    except IOError as e:
        print(f"Error while writing to file: {e}")


# Step 5: Main function to execute the tool
def main():
    """
    Main function to manage user input and execute the weather data retrieval process.
    """
    print("=== Weather Data Retrieval Tool ===")

    # User input
    city_name = input("Enter city name: ").strip()
    state_name = input("Enter state name (optional): ").strip()
    country_name = input("Enter country name (optional): ").strip()

    # Validate date input
    start_date = input("Enter the start date (YYYY-MM-DD): ").strip()
    while not validate_date(start_date):
        print("Invalid date format. Please enter a valid date (YYYY-MM-DD).")
        start_date = input("Enter the start date (YYYY-MM-DD): ").strip()

    end_date = input("Enter the end date (YYYY-MM-DD): ").strip()
    while not validate_date(end_date):
        print("Invalid date format. Please enter a valid date (YYYY-MM-DD).")
        end_date = input("Enter the end date (YYYY-MM-DD): ").strip()

    # Specify output folder
    output_folder = input("Enter the path to store the output file: ").strip()

    try:
        # Retrieve coordinates and fetch weather data
        latitude, longitude = get_coordinates(city_name, state_name, country_name)
        fetch_weather_data(latitude, longitude, start_date, end_date, city_name, output_folder)
    except Exception as e:
        print(e)


# Run the script
if __name__ == "__main__":
    main()
