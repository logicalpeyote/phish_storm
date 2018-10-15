# phish_storm

Phish_Storm è stato creato con lo scopo di mandare email di phishing eludendo i vari filtri antispam
(google, exchange ecc)

si tratta di un piccolo server SMTP pensato unicamente per fare phishing, quindi utilizzando lui al posto di postfix (o quello che usate di solito) il giro sarà questo

Applicativo X per il phishing ~> Phish_Storm ~> TOR ~> 000webhost ~> Casella Exchange

Phish_Storm è stato testato con GoPhisher, ma puo potenzialmente essere utilizzato con qualsiasi altro applicativo che consenta di scegliere il server SMTP

il servizio ascolta sulla porta 1025 del localhost

# prerequisiti

Tor installato sulla macchina 

python3 

moduli python3
smtpd, asyncore, email, requests, stem, time, random

# configurazione

POOL WEBHOST ~> variabile URL

Per evitare il BAN dell' host, occorrono una decina o piu webhost, tutti contenenti solo il file send.php,
verranno scelti in maniera randomica e utilizzati sempre con un ip di tor diverso, piu sono e meglio è, 

registrati qui ~> https://it.000webhost.com
      
dovete creare account su 000webhost e aggiungerli al Pool nella variabile URL
per l' email utilizzatela temporanea, questo sito funziona per 000webhost ~> https://temp-mail.org/it/

una volta creato per ogni webhost dovete uploadare il file send.php e poi aggiungere il link alla lista( vedi gli esempi nella variabile URL)

API KEY ~> variabile API

per impedire a chiunque di utilizzare uno dei vostri host, il file send.php contiene una api key, che va settata uguale anche nella variabile API del python

TOR

il parametro

ControlPort 9051

va abilitato dentro il file torrc, tutto il resto deve essere lasciato commentato


# Credits

Copyright © 2018 by Luca Morini & Giuseppe Cristofaro.

Il codice puo liberamente essere condiviso o modificato, a patto di mantenere il credit all' interno.

