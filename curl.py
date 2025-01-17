import requests
import time


# URL of the endpoint
url = "http://129.65.51.244:5000/login"

# Data to send in the POST request
data = {
    "user": "ayaank",
    "password": "PasswordHere"
}
#start_time = time.time()
# Send the POST request
#response = requests.post(url, data=data)
#end_time = time.time()
# Print the response
print(f"Status Code: {response.status_code}")
print("Response Text:")
print(response.text)
#curl_time = end_time - start_time

#print(curl_time)


def curl(iterations):
        
    for 
        data = {
            "user": "ayaank",
            "password": "PasswordHere"
        }
        start_time = time.time()
# Send the POST request
        response = requests.post(url, data=data)
        end_time = time.time()
# Print the response
        print(f"Status Code: {response.status_code}")
        print("Response Text:")
        print(response.text)
        curl_time = end_time - start_time

        print(curl_time)
