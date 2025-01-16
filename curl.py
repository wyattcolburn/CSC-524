import requests

# URL of the endpoint
url = "http://129.65.51.244:5000/login"

# Data to send in the POST request
data = {
    "user": "ayaank",
    "password": "PasswordHere"
}

# Send the POST request
response = requests.post(url, data=data)

# Print the response
print(f"Status Code: {response.status_code}")
print("Response Text:")
print(response.text)

