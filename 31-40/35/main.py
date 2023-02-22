from twilio.rest import Client 
 
account_sid = 'AC24ef17de3e4f6e0373ce1358a7e9844f' 
auth_token = '079a635270ce203732be11b1c53681a8' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(         
                              to='+13192150144',
                              from_='+17622426653',
                              body="twilios sucka deez nuts" 
                          ) 
 
print(message.sid)