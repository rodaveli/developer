import requests
import json
from database import get_all_voters

GOOGLE_GEOCODE_API_KEY = "AIzaSyDM5zZdZCOfguxHyDESvEhzxVJIOeqmGto"
GOOGLE_MAP_API_KEY = "AIzaSyDM5zZdZCOfguxHyDESvEhzxVJIOeqmGto"

def geocode_address(address):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={GOOGLE_GEOCODE_API_KEY}"
    response = requests.get(url)
    data = json.loads(response.text)
    if data["status"] == "OK":
        location = data["results"][0]["geometry"]["location"]
        return location["lat"], location["lng"]
    else:
        return None

def get_voters_in_radius(center_lat, center_lng, radius):
    all_voters = get_all_voters()
    voters_in_radius = []

    for voter in all_voters:
        voter_lat, voter_lng = voter["location"]
        distance = ((voter_lat - center_lat) ** 2 + (voter_lng - center_lng) ** 2) ** 0.5
        if distance <= radius:
            voters_in_radius.append(voter)

    return voters_in_radius

def filter_voters_by_attribute(voters, attribute, value):
    filtered_voters = [voter for voter in voters if voter[attribute] == value]
    return filtered_voters