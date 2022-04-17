import requests


def get_dateset():
    response = requests.get("https://data.cityofnewyork.us/api/views/7yc5-fec2/rows.json?accessType=DOWNLOAD").json()
    return response