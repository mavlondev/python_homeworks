# ### Task 1

# Scrape weather information from an HTML file and process it using Python and BeautifulSoup.

# <h4>5-Day Weather Forecast</h4>
# <table>
#     <thead>
#         <tr>
#             <th>Day</th>
#             <th>Temperature</th>
#             <th>Condition</th>
#         </tr>
#     </thead>
#     <tbody>
#         <tr>
#             <td>Monday</td>
#             <td>25°C</td>
#             <td>Sunny</td>
#         </tr>
#         <tr>
#             <td>Tuesday</td>
#             <td>22°C</td>
#             <td>Cloudy</td>
#         </tr>
#         <tr>
#             <td>Wednesday</td>
#             <td>18°C</td>
#             <td>Rainy</td>
#         </tr>
#         <tr>
#             <td>Thursday</td>
#             <td>20°C</td>
#             <td>Partly Cloudy</td>
#         </tr>
#         <tr>
#             <td>Friday</td>
#             <td>30°C</td>
#             <td>Sunny</td>
#         </tr>
#     </tbody>
# </table>


# Assume you are given the following HTML structure (you can save it as `weather.html`):

# html
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Weather Forecast</title>
# </head>
# <body>
#     <h4>5-Day Weather Forecast</h4>
#     <table>
#         <thead>
#             <tr>
#                 <th>Day</th>
#                 <th>Temperature</th>
#                 <th>Condition</th>
#             </tr>
#         </thead>
#         <tbody>
#             <tr>
#                 <td>Monday</td>
#                 <td>25°C</td>
#                 <td>Sunny</td>
#             </tr>
#             <tr>
#                 <td>Tuesday</td>
#                 <td>22°C</td>
#                 <td>Cloudy</td>
#             </tr>
#             <tr>
#                 <td>Wednesday</td>
#                 <td>18°C</td>
#                 <td>Rainy</td>
#             </tr>
#             <tr>
#                 <td>Thursday</td>
#                 <td>20°C</td>
#                 <td>Partly Cloudy</td>
#             </tr>
#             <tr>
#                 <td>Friday</td>
#                 <td>30°C</td>
#                 <td>Sunny</td>
#             </tr>
#         </tbody>
#     </table>

# </body>
# </html>



# 1. **Parse the HTML File**:
#    - Load the `weather.html` file using BeautifulSoup and extract the weather forecast details.

# 2. **Display Weather Data**:
#    - Print the **day**, **temperature**, and **condition** for each entry in the forecast.

# 3. **Find Specific Data**:
#    - Identify and print the day(s) with:
#      - The highest temperature.
#      - The "Sunny" condition.

# 4. **Calculate Average Temperature**:
#    - Compute and print the **average temperature** for the week.

# ---

# ### Task 2

# Scrape job listings from the website https://realpython.github.io/fake-jobs and store the data into an SQLite database.

# 1. **Scraping Requirements**:
#    - Extract the following details for each job listing:
#      - **Job Title**
#      - **Company Name**
#      - **Location**
#      - **Job Description**
#      - **Application Link**

# 2. **Data Storage**:
#    - Store the scraped data into an SQLite database in a table named `jobs`.

# 3. **Incremental Load**:
#    - Ensure that your script performs **incremental loading**:
#      - Scrape the webpage and add only **new job listings** to the database.
#      - Avoid duplicating entries. Use `Job Title`, `Company Name`, and `Location` as unique identifiers for comparison.

# 4. **Update Tracking**:
#    - Add functionality to detect if an existing job listing has been updated (e.g., description or application link changes) and update the database record accordingly.

# 5. **Filtering and Exporting**:
#    - Allow filtering job listings by **location** or **company name**.
#    - Write a function to export filtered results into a CSV file.


# ### Task 3

# You are tasked with scraping laptop data from the "Laptops" section of the [Demoblaze website](https://www.demoblaze.com/) and storing the extracted information in JSON format.

# **Steps:**

# 1. **Navigate to the Website:**
#    - Visit the [Demoblaze homepage](https://www.demoblaze.com/).
#    - Click on the **Laptops** section to view the list of available laptops.

# 2. **Navigate to the Next Page:**
#    - After reaching the Laptops section, locate and click the **Next** button to navigate to the next page of laptop listings.

# 3. **Data to Scrape:**
#    For each laptop on the page, scrape the following details:
#    - **Laptop Name**
#    - **Price**
#    - **Description**

# 4. **Data Storage:**
#    - Save the extracted information in a structured **JSON format** with fields like:
     

# json
#      [
#        {
#          "name": "Laptop Name",
#          "price": "Laptop Price",
#          "description": "Laptop Description"
#        },
#        ...
#      ]
     
#tast1
import json
from bs4 import BeautifulSoup

# Load the HTML file
with open('weather.html', 'r') as file:
    html_content = file.read()
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
# Extract the weather forecast details
forecast_table = soup.find('table')
# Initialize a list to store the weather data
weather_data = []
# Iterate through the rows of the table body
for row in forecast_table.tbody.find_all('tr'):
    day = row.find_all('td')[0].text
    temperature = row.find_all('td')[1].text
    condition = row.find_all('td')[2].text
    weather_data.append({
        'day': day,
        'temperature': temperature,
        'condition': condition
    })
# Display the weather data
for entry in weather_data:
    print(f"Day: {entry['day']}, Temperature: {entry['temperature']}, Condition: {entry['condition']}")
# Find the day(s) with the highest temperature
max_temp = max(int(entry['temperature'].replace('°C', '')) for entry in weather_data)
hottest_days = [entry['day'] for entry in weather_data if int(entry['temperature'].replace('°C', '')) == max_temp]
print(f"Day(s) with the highest temperature ({max_temp}°C): {', '.join(hottest_days)}")
# Find the day(s) with "Sunny" condition
sunny_days = [entry['day'] for entry in weather_data if entry['condition'] == 'Sunny']
print(f"Day(s) with 'Sunny' condition: {', '.join(sunny_days)}")
# Calculate the average temperature for the week
average_temp = sum(int(entry['temperature'].replace('°C', '')) for entry in weather_data) / len(weather_data)
print(f"Average temperature for the week: {average_temp:.2f}°C")

# task2
import sqlite3
import requests
from bs4 import BeautifulSoup
# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('jobs.db')   
cursor = conn.cursor()
# Create the jobs table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS jobs (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    company TEXT,
                    location TEXT,
                    description TEXT,
                    application_link TEXT
                )''')
# Function to scrape job listings
def scrape_jobs():
    url = 'https://realpython.github.io/fake-jobs'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    job_cards = soup.find_all('div', class_='card-content')
    for job in job_cards:
        title = job.find('h2', class_='title').text.strip()
        company = job.find('h3', class_='company').text.strip()
        location = job.find('p', class_='location').text.strip()
        description = job.find('p', class_='description').text.strip()
        application_link = job.find('a')['href']
        # Check for duplicates
        cursor.execute("SELECT * FROM jobs WHERE title=? AND company=? AND location=?", (title, company, location))
        existing_job = cursor.fetchone()
        if existing_job:
            # Check for updates
            if existing_job[4] != description or existing_job[5] != application_link:
                cursor.execute("UPDATE jobs SET description=?, application_link=? WHERE id=?", (description, application_link, existing_job[0]))
                print(f"Updated job: {title} at {company}")
        else:
            cursor.execute("INSERT INTO jobs (title, company, location, description, application_link) VALUES (?, ?, ?, ?, ?)", (title, company, location, description, application_link))
            print(f"Added new job: {title} at {company}")
    conn.commit()

# Function to filter jobs by location or company name   
def filter_jobs(filter_type, filter_value):
    if filter_type == 'location':
        cursor.execute("SELECT * FROM jobs WHERE location=?", (filter_value,))
    elif filter_type == 'company':
        cursor.execute("SELECT * FROM jobs WHERE company=?", (filter_value,))
    return cursor.fetchall()
# Function to export filtered results into a CSV file
def export_to_csv(filtered_jobs, filename):
    import csv
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title', 'Company', 'Location', 'Description', 'Application Link'])
        for job in filtered_jobs:
            writer.writerow(job[1:])  # Skip the ID field
# Example usage
scrape_jobs()
filtered_jobs = filter_jobs('location', 'New York')
export_to_csv(filtered_jobs, 'filtered_jobs.csv')

# task3
import json
import requests
from bs4 import BeautifulSoup
# Function to scrape laptop data
def scrape_laptops():
    url = 'https://www.demoblaze.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    laptops = []
    laptop_cards = soup.find_all('div', class_='card h-100')
    for card in laptop_cards:
        name = card.find('h4', class_='card-title').text.strip()
        price = card.find('h5').text.strip()
        description = card.find('p', class_='card-text').text.strip()
        laptops.append({
            'name': name,
            'price': price,
            'description': description
        })
    return laptops
# Scrape laptop data and save to JSON
laptop_data = scrape_laptops()
with open('laptops.json', 'w') as json_file:
    json.dump(laptop_data, json_file, indent=4)
