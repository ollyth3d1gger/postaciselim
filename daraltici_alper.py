
import requests
import json
import sys



def telegramid():
    raw_token = get_json()
    response = requests.get("https://api.telegram.org/bot"+str(get_token())+"/getUpdates")
    r2= json.loads(response.text)
    resulttext = len(r2['result'])

    i = resulttext-1
    while i > 0:
        if r2['result'][i]['message']['chat']['id'] is not None:
            return r2['result'][i]['message']['chat']['id']
              
        else:
       
            return raw_token['chat']
         

def get_json():
    f = open('creds.json')
 
    data = json.load(f)


    return data
def get_token():
    raw_token = get_json()
    
    return raw_token['key'] 
    

def telegram_bot_sendtext(bot_message):
    bot_chatID = str(telegramid())
    bot_token = get_token()
    
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
for line in iter(sys.stdin.readline, ''):
     telegram_bot_sendtext(line)
