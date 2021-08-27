import requests
import datetime as dt

from requests.api import head

# Step 1: Setting upa a user account on Pixe-la

USERNAME = "siddheshsule47"
TOKEN = "f43rty54h356h3g4g"
GRAPH_ID = "graph3"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor": "yes"
    
}
# response = requests.post(url = pixela_endpoint, json = user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name":"Reading Tracker",
    "unit": "No. of pages",
    "type":"int",
    "color":"ajisai",
}

headers ={
    "X-USER-TOKEN" : TOKEN,
}



# response = requests.post(url = graph_endpoint, json = graph_config, headers = headers)
# print(response.text)


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = dt.datetime(year=2021, month=8,day=27)

print(today)

pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"15",
}

# response = requests.post(url=pixel_creation_endpoint, json= pixel_data, headers=headers )
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "20"
}

response = requests.put(url=update_endpoint, json = new_pixel_data, headers=headers)
print(response.text)