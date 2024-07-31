import requests
import os
from dotenv import load_dotenv
load_dotenv()


def get_meet_id(token):
    url = "https://api.videosdk.live/v2/rooms"
    headers = {
        "authorization": token,
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json={})
    response_data = response.json()
    room_id = response_data.get("roomId")
    print(room_id)
    return room_id 

def get_meet_details():
    meet_id= get_meet_id(os.environ.get("meet_token"))
    token=os.environ.get("meet_token")
    url = "https://api.videosdk.live/v2/rooms/" + meet_id
    headers = {'Authorization' : '"f{token}' ,'content_type': 'application/json'}
    response = requests.get(url="f{url}",headers = headers)
    return response