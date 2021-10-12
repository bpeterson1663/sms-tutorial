from twilio.rest import Client

account_sid = 'ACCOUNT_SID'
auth_token = 'AUTH_TOKEN'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='SID',
    body='This is Brady I am sending this to you from a program I just wrote!',
    to='TO NUMBER'
)

print(message.sid)
