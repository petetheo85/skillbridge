# SkillBridge Opportunities Scraper

## Overview

The [DoD Skillbridge](https://skillbridge.osd.mil) program is an initiative designed to provide service members with valuable civilian work experience through specific industry training, apprenticeships, or internships during their last 180 days of service. This program connects transitioning service members with industry partners, offering real-world job experiences at no cost to the industry partners. Service members continue to receive their military compensation and benefits while gaining invaluable civilian career training.

## Why This Script Was Created

The user interface and searching features on the official SkillBridge website are not user-friendly and make it challenging to find opportunities based on multiple criteria. This script was created to scrape the SkillBridge opportunities and provide a more accessible way to search and analyze the data. By organizing the data into a structured format, users can easily search and filter opportunities based on their specific needs.

## How the Script Works

This script automates the process of scraping the SkillBridge opportunities from the official SkillBridge website and saves the data into an Excel file. It uses Selenium for web scraping and BeautifulSoup for parsing the HTML content. The script navigates through the paginated results, collects the data, and formats it into an Excel file with specified column widths.

### Key Features

- **Automated Data Scraping**: Uses Selenium to navigate through pages and scrape data.
- **HTML Parsing**: Uses BeautifulSoup to parse and extract data from the HTML content.
- **Excel Export**: Organizes the scraped data into an Excel file with customizable column widths.
- **User-Friendly Data**: Provides a more accessible way to search and analyze SkillBridge opportunities.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/petetheo85/skillbridge.git
   cd skillbridge
   ```

2. **Download ChromeDriver**:
   Ensure you have the Chrome browser installed, then download the corresponding ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in your project directory.
   
## Usage

1. **Run the Script**:
   ```bash
   python skillbridge.py
   ```

2. **Check the Output**:
   The scraped data will be saved in an Excel file named `DoD_SkillBridge_Data.xlsx` in the project directory.

### Script Explanation

The script performs the following steps:

1. **Set up the WebDriver and open the URL**:
   Initializes the Selenium WebDriver and navigates to the SkillBridge locations page.

2. **Wait for the page to load and click the search button**:
   Waits for the search button to be clickable and then clicks it to display the results.

3. **Scrape the data**:
   Parses the HTML content using BeautifulSoup and extracts the table data.

4. **Handle pagination**:
   Continues to scrape data from subsequent pages until all entries are collected.

5. **Save the data to an Excel file**:
   Formats the data into a pandas DataFrame, drops unnecessary columns, and exports it to an Excel file with specified column widths.

### Configuration

The column widths and the headers to be dropped can be configured in the script. Here is the relevant part of the code:

```python
df = df.drop(columns=['Actions', 'MOU Organization'])  # unnecessary columns

# Set standard column widths
standard_width = {
    "Partner/Program/Agency": 40,
    "Service": 20,
    "City": 20,
    "State": 10,
    "Duration of Training": 20,
    "Employer POC": 20,
    "POC Email": 30,
    "Cost": 25,
    "Closest Installation": 25,
    "Opportunity Locations by State": 20,
    "Delivery Method": 20,
    "Target MOCs": 20,
    "Other Eligibility Factors": 20,
    "Other/Prerequisite": 100,
    "Jobs Description": 100,
    "Summary Description": 100,
    "Job Family": 30
}

```

## Contribution

Contributions are welcome! Please open an issue or submit a pull request with any changes or improvements.


## Acknowledgements

Special thanks to the DoD SkillBridge program for providing such valuable opportunities to transitioning service members.


