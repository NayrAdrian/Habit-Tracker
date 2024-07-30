import requests
from datetime import datetime

USERNAME = "nayradrian"  # Chosen Username
TOKEN = "hkKdfhdasiHlg931tyaw412s"  # Personalized Token (Personal)
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

# Parameters for setting up a new account
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",  # Agreement to the terms of service
    "notMinor": "yes",  # Confirmation that the user is not a minor
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Define the endpoint for creating a new graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Configuration for the new graph
graph_config = {
    "id": "graph1",  # Unique identifier for the graph
    "name": "Jogging Graph",  # Name of the graph
    "unit": "Km",  # Unit of measurement
    "type": "float",  # Data type (float for decimal numbers)
    "color": "sora"  # Color of the graph
}

# Headers for the request, including the authentication token
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "8.2",
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)