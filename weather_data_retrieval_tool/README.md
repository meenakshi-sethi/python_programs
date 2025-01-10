# 🌦️ Weather Data Retrieval Tool  

A Python-based solution to fetch **historical weather data** for any city worldwide. This tool integrates APIs for **geocoding** and **weather data fetching**, making it an excellent intermediate-level project for anyone looking to expand their Python skills.  

If you're familiar with Python basics (like loops, conditionals and functions) and want to practice working with APIs, file handling and input validation, this project is for you!  

---

## ✨ Features  

### 🌍 Dynamic Location Input  
- Enter any city name, with optional state and country details.  
- Automatically converts the city name into latitude and longitude.  

### 📅 Custom Date Range  
- Specify the start and end dates to get precise weather data for your needs.  

### 💾 CSV Export  
- Automatically saves the weather data into a well-organized CSV file.  

### 📁 Custom Output Directory  
- Allows you to choose where the file will be saved, ensuring flexibility.  

### 🔐 Secure API Handling  
- Masks API keys in logs to keep your sensitive information secure.  

---

## 🛠️ Installation & Setup  

### Prerequisites  
- **Python**: Version 3.7 or higher.  
- **Libraries**: Install the required Python libraries:  
  ```bash
  pip install requests
  ```  

### Steps to Use  
1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/yourusername/weather-data-retrieval-tool.git
   cd weather-data-retrieval-tool
   ```  

2. **Get an OpenCage API Key**:  
   - Sign up at [OpenCage](https://opencagedata.com/) to get your free API key (2,500 free requests/day).  

3. **Update the Script**:  
   Open `weather_data_tool.py` and update the following:  
   - **Add your OpenCage API Key**:  
     Replace the placeholder with your actual API key:  
     ```python
     api_key = "your_api_key"  
     ```  

   - **Set the Path for Saving the CSV File**:  
     Specify the folder where you want the CSV files to be saved in the `fetch_weather_data` function:
     ```python
     output_folder = "your_desired_path"  # Replace with the directory where you want to save the CSV files
     ```  

4. **Run the Program**:  
   ```bash
   python weather_data_tool.py
   ```  

5. **Follow the Prompts**:  
   - Enter the city, state, country, date range, and the path where you want to save the output file.  

---

## 🌟 Example Output  

### User Input:  
```text
Enter the city name: Boston  
Enter the state name (optional): MA  
Enter the country name (optional): USA  
Enter the start date (YYYY-MM-DD): 2024-05-01  
Enter the end date (YYYY-MM-DD): 2024-08-31  
Enter the path to store the output file: /your/desired/path
```  

### Generated CSV File:  
**File Name**: `Boston_weather_data.csv`  

| Date       | Max Temp (°C) | Min Temp (°C) | Precipitation (mm) | Max Wind Speed (km/h) |  
|------------|---------------|---------------|---------------------|------------------------|  
| 2024-05-01 | 20.1          | 12.3          | 0.0                 | 15.0                  |  
| 2024-05-02 | 22.0          | 14.2          | 1.2                 | 18.0                  |  


[View Code]()
---

## 🌐 API Information  

### 1️⃣ OpenCage Geocoder API  
- **Purpose**: Converts city names into latitude and longitude.  
- **Free Limit**: 2,500 requests/day for non-commercial use.  
- **Why OpenCage?**:  
  - Reliable results, even for ambiguous city names.  
  - Chosen over OpenStreetMap Nominatim, which had reliability issues.  

### 2️⃣ OpenStreetMap Nominatim API (Tried Previously)  
- **Purpose**: Converts city names into latitude and longitude.  
- **Issue**: Encountered errors fetching results, even after adding recommended headers.  
- **Notes**: Intended for light usage only.  

### 3️⃣ Open-Meteo Weather API  
- **Purpose**: Fetches historical weather data for specified coordinates.  
- **Free Limit**: Unlimited fair usage for personal/educational projects.  
- **Data Provided**:  
  - Daily max/min temperatures.  
  - Precipitation.  
  - Wind speed.  

---

## 💡 Why This Is Intermediate-Level  

- **API Integration**:  
  Uses two APIs (OpenCage and Open-Meteo) with GET requests and JSON parsing.  

- **Error Handling**:  
  Implements structured error handling to manage invalid inputs, API failures and file system issues.  

- **Input Validation**:  
  Ensures that dates are entered in the correct format (`YYYY-MM-DD`).  

---

## 🔮 Future Improvements  

Here are some ideas to make this project even better:  
- Add support for fetching data for multiple cities in one run.  
- Include additional weather parameters (e.g., humidity, UV index).  
- Visualize weather trends with graphs using libraries like Matplotlib or Plotly.  
- Build a web app version using Flask or Django.  

---

## 📜 License  

This project is licensed under the MIT License. Feel free to use, modify, or share it, as long as you include this notice.  

---

## 📝 Final Thoughts  

This project helped me level up my Python skills by exploring API integration, file handling and input validation. It's a great step forward if you're familiar with Python basics and want to try building something practical.  
