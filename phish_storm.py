#!/usr/bin/env python3

import smtpd
import asyncore
import email
from email.header import decode_header
import requests
from stem import Signal
from stem.control import Controller
import time
import random


'''
POOL WEBHOST
https://it.000webhost.com

Per evitare il BAN dell' host, occorrono una decina o piu webhost, tutti contenenti solo il file send.php,
verranno scelti in maniera randomica e utilizzati sempre con un ip di tor diverso
      
dovete creare account su 000webhost e aggiungerli al Pool nella variabile URL
per l' email utilizzatela temporanea, questo sito funziona per 000webhost ~> https://temp-mail.org/it/
'''

RESOURCE = '/send.php'
URL= [	'https://socknew123.000webhostapp.com', 
		'https://esc2auto.000webhostapp.com', 
		'https://cazzocazzo.000webhostapp.com', 
		'https://sdfdsfafdsaf.000webhostapp.com', 
		'https://werweqreqwr.000webhostapp.com', 
		'https://jdsgfdgdfhsfdh.000webhostapp.com',
		'https://sadfhjmhgsfjgahdfgsf.000webhostapp.com', 
		'https://mbnvczxsdf.000webhostapp.com', 
		'https://adwerwrew.000webhostapp.com', 
		'https://sdafjasdsfafgshgat1thecitybiz.000webhostapp.com', 
		'https://qergrqofgenfgsq.000webhostapp.com', 
		'https://werqegfdagadg.000webhostapp.com/', 
		'https://dsgqdgvdfanovadfngo.000webhostapp.com', 
		'https://vsdyasfhdsfuewqtqertgfdgfadgadfydr.000webhostapp.com'] 
		


API = "YOUR_API_KEY"
HOST = '127.0.0.1' 
PORT = 1025
SMTPheader = { 'Content-Type': 'application/x-www-form-urlencoded' }
PROXY = {'http': 'socks5://127.0.0.1:9050','https': 'socks5://127.0.0.1:9050'}
MYIP = 'https://api.ipify.org?format=json'
TOR_CONTROLLER_PORT = 9051
REQUESTS_INTERVAL = 30

class CustomSMTPServer(smtpd.SMTPServer):
    random.seed(74856)
    def process_message(self, peer, frm, to, data):
        msg = email.message_from_string(data)
        mail_to = str(to[0])
        subject, mail_from, body = self.decode_message(msg)
        self.renew_tor()
        PAR = {'to': mail_to, 'subject': subject, 'from' : mail_from, 'message': body, 'api': API}
        url = self.choose_host()
        print('###################################')	
        print("Relay: %s" % url)
        print("From: %s" % mail_from)
        print("to: %s" % mail_to)
        print("subject: %s" % subject)	
        requests.post(lrl + RESOURCE, headers=SMTPheader, data=PAR, proxies=PROXY)

#######################################################################################################
#FUNZIONI
#######################################################################################################
    def renew_tor(self):
        with Controller.from_port(port = TOR_CONTROLLER_PORT) as controller:
            controller.authenticate()	
            controller.signal(Signal.NEWNYM)
            controller.close()
            print("Acquisizione ip tor")
            time.sleep(REQUESTS_INTERVAL)			
            response = requests.get(MYIP, proxies=PROXY)
            print('tor ip: {}'.format(response.text.strip()))
	
    def decode_message(self,msg):
        subject = ''
        mail_from = ''
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                ctype = part.get_content_type()
                cdispo = str(part.get('Content-Disposition'))
                if ctype == 'text/plain' and 'attachment' not in cdispo:
                    body = part.get_payload(decode=True)
                    break
                else:
                    body = msg.get_payload(decode=True)

                for encoded_string, charset in decode_header(msg.get('Subject')):
                    try:
                        if charset is not None:
                            subject += encoded_string.decode(charset)
                        else:
                            subject += encoded_string
                    except:
                        pass

                for encoded_string, charset in decode_header(msg.get('From')):
                    try:
                        if charset is not None:
                            mail_from += encoded_string.decode(charset)
                        else:
                            mail_from += encoded_string
                    except:
                        pass
			    
            return subject, mail_from, body
	
    def choose_host(self):
        n = random.randint(0, len(URL)-1)
        return URL[n]
		
server = CustomSMTPServer((HOST,PORT), None)

asyncore.loop()
