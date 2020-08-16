 
import urllib.request
import urllib.parse
 
def sendSMS(apikey, numbers, sender, message):
    apikey = 'WvimlpcZ0RM-7Ir8OM0v7gBOiufsNCVlmMl9PegsUv'
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': '917470400587',
        'message' : 'message',})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)
 
resp =  sendSMS('apikey', '918878052110',
    'Ragini Kalvade', 'This is your message')
print (resp)