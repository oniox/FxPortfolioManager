
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from fxpmgr.utils import ConfigUtil



def sendmail(content):
    recipient = ConfigUtil.getReceiver()    
    sender = ConfigUtil.getSender()

    msg = MIMEText(str(content))
    msg['Subject'] = 'FXManagerPortfolio alert %s' %datetime.now().strftime('%d/%m/%y %H:%M')
    msg['From'] = sender 
    msg['To'] = recipient
    
    print 'EMailing the following content to client :\n Subject: {0} \n Text: {1}'.format(msg['Subject'],content)

    #s = smtplib.SMTP(ConfigUtil.getSmtpHost().strip())
    #s.login(properties[PROP_SMTP_USER].strip(), '')
    #s.sendmail(sender, [recipient], msg.as_string())
    #s.quit()
