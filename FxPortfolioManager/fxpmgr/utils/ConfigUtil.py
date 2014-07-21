from  ConfigParser import ConfigParser

configp = ConfigParser()
configp.read("../../resources/fxpmgr.ini")


def getFileDirectory():
    return configp.get('RatesData', 'rates.dir')
    
def getDefaultRates():
    return configp.get('RatesData', 'rates.default')

def getSmtpHost():
    return configp.get('Email', 'smtp.host')

def getSmtpUser():
    return configp.get('Email', 'smtp.user')

def getSender():
    return configp.get('Email', 'sender')

def getReceiver():
    return configp.get('Email', 'receiver')


    

# def main():
#     cfgfile = open("../../resources/fxpmgr.ini", 'w')
#     configp = ConfigParser()
#     configp.add_section('RatesData')
#     configp.set('RatesData', 'rates.default', ['GBP/USD','GBP/JPY', 'GBP/AUD', 'CAD/GBP', 'CNY/GBP'])    
#     configp.set('RatesData', 'rates.dir', '../../data')
#      
#     configp.add_section('Email')
#     configp.set('Email','smtp.host', 'smtp.google.com')
#     configp.set('Email','smtp.user', 'client')
#     configp.set('Email','sender', 'sender@gmail.com')
#     configp.set('Email','receiver', 'receiver@gmail.com')
#      
#     configp.write(cfgfile)
#     cfgfile.close()
     
    
    
# if __name__ == "__main__":
#     main()
     
    
    