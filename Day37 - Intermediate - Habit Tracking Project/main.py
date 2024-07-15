import requests
from datetime import datetime

USERNAME = "_YOUR_USERNAME_"  # use your own credentials
TOKEN = "_YOUR_TOKEN_"        # use your own credentials
GRAPH_ID = "graph01"

api_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=api_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{api_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "my graph",
    "unit": "km",
    "type": "float",
    "color": "sora",
}

header = {
    "X-USER-TOKEN": TOKEN,
}

# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=header)
# print(graph_response.text)

pixel_endpoint = f"{api_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you travel today?"),
}

pixel_response = requests.post(url=pixel_endpoint, json=pixel_params, headers=header)
print(pixel_response.text)

update_endpoint = f"{api_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "7",
}

# update_response = requests.put(url=update_endpoint, json=new_pixel_data, headers=header)
# print(update_response.text)


delete_endpoint = f"{api_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# delete_response = requests.delete(url=delete_endpoint, headers=header)
