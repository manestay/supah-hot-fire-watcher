# TODO: place this code when the danger page renders
from twilio.rest import TwilioRestClient
import time
def send(room):
    t = time.strftime('%H:%M:%S, %d %b %Y')

    # the following line needs your Twilio Account SID and Auth Token
    client = TwilioRestClient("ACe7e8d8d1b382c5db537f79dd12e8113c", "3124f9c0ca870aa93916ceceda8674f1")

    # change the "from_" number to your Twilio number and the "to" number
    # to the phone number you signed up for Twilio with, or upgrade your
    # account to send SMS to any phone number
    client.messages.create(to="+19493108713", from_="+19495417247",
                           body="There is a fire in {} at {}. Open the Supah Hot Fire Watcher for the fastest, safest escape route.".format(room, t))
