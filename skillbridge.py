import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from openpyxl import load_workbook

# Set up the WebDriver and open URL
driver = webdriver.Chrome()
driver.get('https://skillbridge.osd.mil/locations.htm')

# Wait for page to load, scroll search button into view, click using JavaScript
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'loc-search-btn'))
)

driver.execute_script("arguments[0].scrollIntoView();", search_button)
time.sleep(1)  # Wait for any potential overlays to finish loading
driver.execute_script("arguments[0].click();", search_button)

# Wait for the table to be loaded
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'location-table'))
)

all_data = []


def scrape_page():
    """
    Parse the page source and find the table containing the desired data.
    Append each cell to a list; append that list to a list of all data.
    :return: None
    """
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find('table', {'id': 'location-table'})
    tbody = table.find('tbody')

    for row in tbody.find_all('tr', {'role': 'row'}):
        row_data = []
        for cell in row.find_all('td'):
            row_data.append(cell.get_text(strip=True))
        all_data.append(row_data)


while True:
    scrape_page()

    # Check if we are on the last page (find "Showing XXX of XXX entries")
    status_text = driver.find_element(By.ID, 'location-table_info').text
    if "of" in status_text:
        total_entries = int(status_text.split("of")[-1].strip().split(" ")[0].replace(',', ''))
        if total_entries == len(all_data):
            break

    try:
        # Find the "Next" link, scroll link into view, click using JavaScript
        next_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'location-table_next'))
        )

        driver.execute_script("arguments[0].scrollIntoView();", next_link)
        driver.execute_script("arguments[0].click();", next_link)
        time.sleep(0.25)

    except Exception as e:
        print(f"Exception encountered: {e}")
        break

driver.quit()  # Close WebDriver

# Define the column headers, convert all data into DataFrame, export to Excel
headers = [
    "Actions", "Partner/Program/Agency", "Service", "City", "State", "Duration of Training", "Employer POC",
    "POC Email", "Cost", "Closest Installation", "Opportunity Locations by State", "Delivery Method", "Target MOCs",
    "Other Eligibility Factors", "Other/Prerequisite", "Jobs Description", "Summary Description", "Job Family",
    "MOU Organization"
]

df = pd.DataFrame(all_data, columns=headers)
df = df.drop(columns=['Actions', 'MOU Organization'])  # unnecessary columns
excel_path = 'DoD_SkillBridge_Data2.xlsx'
df.to_excel(excel_path, index=False)

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

# Load workbook and access the first sheet to set the width for all columns
workbook = load_workbook(excel_path)
sheet = workbook.active

for column in sheet.columns:
    column_letter = column[0].column_letter  # Get the column letter
    col_header = sheet[column_letter + '1'].value  # Get the column header
    if col_header in standard_width:
        sheet.column_dimensions[column_letter].width = standard_width[col_header]

workbook.save(excel_path)