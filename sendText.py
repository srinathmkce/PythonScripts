__author__ = 'user'

from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC4a96c4b1f1de72bfde5aadbbdd4b665f"
auth_token  = "acebf0cf7a9a3c33ecb8febe7e85b621"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Text Msg Sent From Python Code .. Python Rocks !! :-) ",
    to="+919943021012",    # Replace with your phone number
    from_="+1 251-333-2308") # Replace with your Twilio number
print(message.sid)