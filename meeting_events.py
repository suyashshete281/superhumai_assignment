from videosdk import Participant, MeetingEventHandler
from participants_events import MyParticipantEventHandler

class MyMeetingEventHandler(MeetingEventHandler):
    def __init__(self):
        super().__init__()

    def on_meeting_joined(self, data):
        print("Meeting joined:", data)
    
    def on_meeting_left(self, data):
        print("Meeting left:", data)

    def on_participant_joined(self, participant: Participant):
        print("Participant joined:", participant)
        participant.add_event_listener(MyParticipantEventHandler(participant_id=participant.id))

    def on_participant_left(self, participant: Participant):
        print("Participant left:", participant)

    def on_participant_joined(self, participant):
     print("Participant joined:", participant)
     participant.add_event_listener(MyParticipantEventHandler(participant_id=participant.id))    