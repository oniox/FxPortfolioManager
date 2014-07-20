
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

PROP_SMTP_HOST='mail.smtp.host'
PROP_SMTP_USER='mail.user'
PROP_SENDER_EMAIL='mail.from'
PROP_CLIENT_EMAIL='mail.to'

def sendmail(content, properties):
    recipient = properties[PROP_CLIENT_EMAIL].strip()    
    sender = properties[PROP_SENDER_EMAIL].strip()

    msg = MIMEText(content)
    msg['Subject'] = 'FXManagerPortfolio alert %s' %datetime.now().strftime('%d/%m/%y %H:%M')
    msg['From'] = sender 
    msg['To'] = recipient
    
    print 'E-Mailing the following content to client :\n {0} \n {1}'.format(msg['Subject'],content)

    s = smtplib.SMTP(properties[PROP_SMTP_HOST].strip())
    #s.login(properties[PROP_SMTP_USER].strip(), '')
    #s.sendmail(sender, [recipient], msg.as_string())
    s.quit()
