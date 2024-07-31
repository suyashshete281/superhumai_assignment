from fastapi import APIRouter
from videosdk import MeetingConfig, VideoSDK,RecordingConfig
from meeting_events import MyMeetingEventHandler
import asyncio
import os
from dotenv import load_dotenv
import authentication

load_dotenv()

route=APIRouter( tags=["meet"])

@route.get("/meetings")
async def create_meet():
    meeting_config = MeetingConfig(
        meeting_id= authentication.get_meet_id(os.environ.get("meet_token")),
        name="suyash",
        mic_enabled=True,
        webcam_enabled=True,
        token=os.environ.get("meet_token")
    )
    recording_config = RecordingConfig(
  webhook_url = "path_to_url",
  dir_path="path to storage"
    )
  

   
    meeting = VideoSDK.init_meeting(**meeting_config)
    
    print("joining meet")
    meeting.add_event_listener(MyMeetingEventHandler())
    await meeting.async_join()
    print("meet joined")
    meeting.start_recording(RecordingConfig)
    
    

@route.get("/meetings_details")
def get_details():
 return authentication.get_meet_details()




      
    