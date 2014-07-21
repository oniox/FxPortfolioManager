from fxpmgr.clients.XRatesHttpClient import XRatesHttpClient
from fxpmgr.utils.RatesCalculator import RatesCalculator
from fxpmgr.clients import EmailSenderClient
from fxpmgr.utils import FileSystemUtil
from fxpmgr.clients.XRatesDataClient import XRatesDataClient

'''
 This script sends an email  to specified recipients when exchange rates breaches pre-defined threshold values: 
 
'''
 
def main():
    #   scrape data from xrates - default to GBP as base currency - also fetches its inverse 
    data = XRatesHttpClient("http://www.x-rates.com/table/?from=GBP").getXRatesData()    
    #default data layer is filesystem, can be mongo etc  
    persistRatesData(data)
    reader = XRatesDataClient(getSortedRatesData())
 
    #fetch original rates data 
    initRatesData = reader.getInitialRatesData()
      
    if initRatesData:
        #where only original exists previous and latest rates defers to original
        prevData = reader.getPreviousData()
       
        if not prevData:
            prevData = initRatesData
            
        print "Original data:\n", initRatesData
        print "Previous data:\n", prevData
        print "Latest data:\n", reader.getLatestRatesData()
        print "\n"
        
        overThreshld = RatesCalculator().getRatesAboveThreshold(initRatesData, prevData, reader.getLatestRatesData())
        if overThreshld and len(overThreshld) > 0:
            contents = []
            for tup in overThreshld:                
                contents.append( 'Threshold breached for FXPair: %s , previous rate : %s, latest rate %s' %(tup))
            EmailSenderClient.sendmail(contents)
        else:
            print 'Threshold was not breached' 
    
def persistRatesData(rdata): 
        return FileSystemUtil.writeDictToFile(rdata)   
    
def getSortedRatesData():
        return FileSystemUtil.getSortedData();                   
        
if __name__ == "__main__":
    main()