from fxpmgr.clients.XRatesHttpClient import XRatesHttpClient
from fxpmgr.utils.RatesCalculator import RatesCalculator
from fxpmgr.clients import EmailSenderClient
from fxpmgr.utils import FileSystemUtil
from fxpmgr.clients.XRatesDataClient import XRatesDataClient


 
def main():
#     data = XRatesHttpClient("http://www.x-rates.com/table/?from=GBP").getXRatesData()    
#     persistRatesData(data)
    reader = XRatesDataClient(getSortedRatesData())
 
    initRatesData = reader.getInitialRatesData()
    print initRatesData
      
    if initRatesData:
        prevData = reader.getPreviousData()
        print prevData
        print reader.getLatestRatesData()
        
        if not prevData:
            prevData = initRatesData
        overThreshld = RatesCalculator().getRatesAboveThreshold(initRatesData, prevData, reader.getLatestRatesData())
#         if overThreshld and len(overThreshld) > 0:
#             contents = []
#             for tup in overThreshld:                
#                 contents.append( 'Threshold breached for FXPair: %s , previous rate : %s, latest rate %s' %(tup))
#             EmailSenderClient.sendmail(contents)
#         else:
#             print 'Threshold was not breached' 
    
def persistRatesData(rdata):
        return FileSystemUtil.writeDictToFile(rdata)   
    
def getSortedRatesData():
        return FileSystemUtil.getSortedData();                   
        
if __name__ == "__main__":
    main()