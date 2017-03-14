from twilio.rest import TwilioRestClient

account_sid = "ACe6974da23850574e69bc617a3ca941f3"
auth_token  = "8efc4f861fec9d0544522118172f45e1"

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Python",
    to="+8618967880045",
    from_="+18583539803")

print(message.sid)
