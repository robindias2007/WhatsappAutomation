from twilio.rest import Client

account_sid = 'ACc6a79695d0bd0221b809a1d6f085c955'
auth_token = '1fc1a8d386fac57016dfe43bca3428b1'
client = Client(account_sid, auth_token)

def send_message():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body= 'This is for testing. Have a nice day. I love you',
        to='whatsapp:+919833564323'
    )

    print(message.sid)