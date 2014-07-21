
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
    
    print 'E-Mailing the following content to client :\n {0} \n {1}'.format(msg['Subject'],content)

    #s = smtplib.SMTP(ConfigUtil.getSmtpHost().strip())
    #s.login(properties[PROP_SMTP_USER].strip(), '')
    #s.sendmail(sender, [recipient], msg.as_string())
    #s.quit()
