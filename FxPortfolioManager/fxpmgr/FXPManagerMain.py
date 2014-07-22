from fxpmgr.clients.XRatesHttpClient import XRatesHttpClient
from fxpmgr.utils.RatesCalculator import RatesCalculator
from fxpmgr.clients import EmailSenderClient
from fxpmgr.utils import FileSystemUtil, ConfigUtil
from fxpmgr.clients.XRatesDataClient import XRatesDataClient

'''
 This coordinator script fetches exchange rates data from xrates.com, persists scraped data to filesystem. 
 It coordinates evaluation of rates data (as read from filesystem) against a predefined threshold and triggers 
an email to specified recipients on breach of threshold values 
'''

def main():
    #   scrape data from xrates - default to GBP as base currency - also fetches its inverse 
    data = XRatesHttpClient("http://www.x-rates.com/table/?from=GBP").getXRatesData()    
    #default data layer is filesystem, can be mongo etc  
    persistRatesData(data)
    reader = XRatesDataClient(getSortedRatesData())
 
    #fetch original rates data 
    initRatesData = filterRatesData(reader.getInitialRatesData())
      
    if initRatesData:
        #where only original exists previous and latest rates defers to original
        prevData = filterRatesData(reader.getPreviousData())
       
        if not prevData:
            prevData = initRatesData
                    
        latestData = filterRatesData(reader.getLatestRatesData())            
        print "Original data:\n", initRatesData
        print "Previous data:\n", prevData
        print "Latest data:\n", latestData
        print "\n"
        
        ratesCalc = RatesCalculator(ConfigUtil.getRatesThreshold())
        overThreshld = ratesCalc.getRatesAboveThreshold(initRatesData, prevData, latestData)
        
        if overThreshld and len(overThreshld) > 0:
            contents = []
            for tup in overThreshld:                
                contents.append( 'Threshold breached for FXPair: %s , previous rate : %s, latest rate %s' %(tup))
            EmailSenderClient.sendmail(contents)
        else:
            print 'Threshold was not breached for any of the configured currency pairs' 
    
def persistRatesData(rdata): 
        return FileSystemUtil.writeDictToFile(rdata)   
    
def getSortedRatesData():
        return FileSystemUtil.getSortedData(); 
   
#filter specified rates data by rates defined in config   
def filterRatesData(ratesdata):
    if not ratesdata:
        return ratesdata
    configuredRates = ConfigUtil.getDefaultRates()  
    return {r.strip():float(ratesdata[r.strip()]) for r in configuredRates.split(',') if ratesdata[r.strip()]}
                      
        
if __name__ == "__main__":
    main()