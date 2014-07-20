from utils.XRatesHtmlParser2 import XRatesHtmlParser2
#from clients.XRatesClient import XRatesHttpClient
from clients.XRatesClient import  XRatesHttpClient
from fxpmgr.utils.RatesCalculator import RatesCalculator
from fxpmgr.clients import EmailSenderClient
from fxpmgr.clients import FileSystemUtil
import pickle
import time


 
def main():    
     #FileSystemUtil.writeDictToFile({'a':1, 'b':2, 'c':3})
#     time.sleep(2)
     #FileSystemUtil.writeDictToFile({'a':1, 'b':2, 'c':3})
   
   #print FileSystemUtil.sortFileNames( FileSystemUtil.getFileNames() )
   
   print XRatesHttpClient("http://www.x-rates.com/table/?from=GBP").getXRatesData();
    
    
    
#     favorite_color = { "lion": "yellow", "kitty": "red" }
#     pickle.dump( favorite_color, open( "../../data/save.p", "wb" ) )
    # instantiate the parser and fed it some HTML
    #filehtml = open("c:/Windows/Temp/rates.htm", 'r');
    #print filehtml
    #response = urllib2.urlopen("http://www.x-rates.com/table/?from=GBP")
    #html = response.read()
    #print html
    #parser=  XRatesHtmlParser2()
    #parser.feed('<html><head><title>Test</title></head><body><h1>Parse me!</h1></body></html>')
    # xratesData = parser.feed(html)      
      
    #calc = RatesCalculator()
    #print calc.getRatesAboveThreshold(originalRates={'a': 1.1}, prevRates={'a': 1}, latestRates={'a': 1.2})
    #EmailSenderClient.sendmail('Testing', {EmailSenderClient.PROP_CLIENT_EMAIL : 'client@gmail.com', EmailSenderClient.PROP_SENDER_EMAIL: 'sender@gmail.com',
     #                                EmailSenderClient.PROP_SMTP_HOST : 'smtp.gmail.com', EmailSenderClient.PROP_SMTP_USER : 'sender'})
    
                        
        
if __name__ == "__main__":
    main()