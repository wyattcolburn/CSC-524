import re
import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://csc.calpoly.edu/faculty/'

# Headers to mimic a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

# Send a GET request to the webpage with headers
response = requests.get(url, headers=headers)
response.raise_for_status()  # Ensure the request was successful

# Parse the webpage content
soup = BeautifulSoup(response.text, 'html.parser')

# Convert the soup object to a string
content = str(soup)

# Define a regular expression pattern for matching email addresses
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Find all email addresses in the content
emails = re.findall(email_pattern, content)

# Remove duplicates by converting the list to a set
unique_emails = set(emails)

# Print the extracted email addresses
for email in unique_emails:
    print(email)

