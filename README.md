# phish_storm

Phish_Storm è stato creato con lo scopo di mandare email di phishing eludendo i vari filtri antispam
(google, exchange ecc)

si tratta di un piccolo server SMTP pensato unicamente per fare phishing, quindi utilizzando lui al posto di postfix (o quello che usate di solito) il giro sarà questo

Applicativo X per il phishing ~> Phish_Storm ~> TOR ~> 000webhost ~> Casella Exchange

Phish_Storm è stato testato con GoPhisher, ma puo potenzialmente essere utilizzato con qualsiasi altro applicativo che consenta di scegliere il server SMTP

il servizio ascolta sulla porta 1025 del localhost

# prerequisiti

Tor installato sulla macchina 

ControlPort 9051 abilitato dentro il file torrc

python3 

moduli python3
smtpd, asyncore, email, requests, stem, time, random

# Credits

Copyright © 2018 by Luca Morini & Giuseppe Cristofaro.
Il codice puo liberamente essere condiviso o modificato, a patto di mantenere il credit all' interno.

