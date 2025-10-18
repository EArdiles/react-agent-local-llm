import requests

# Define the server URL
url = "http://127.0.0.1:8000/query"

# Define the query payload
payload = {
    "query": "laptop"
}

# Send the POST request
response = requests.post(url, json=payload)

# Print the response
print("Response from server:", response.json())