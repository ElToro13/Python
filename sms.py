import urllib.request
import urllib.parse
 
def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': 'o72nEm6bzH8-2RcDPpG8PUAaAqI15YzvNzYjXunHjK', 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)
 
resp =  sendSMS('apikey', '917990064641',
    'TXTLCL', 'Hello from Python!')
print (resp)
