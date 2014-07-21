'''
Created on 20 Jul 2014

@author: FN
'''

class XRatesDataClient(object):
    '''
    Rates data provider. Decorates specified sorted rates data and adds convenient access methods.. 
    '''

    sorteddata = []

    def __init__(self, sorteddata):       
        self.sorteddata = sorteddata
    
    
    def getLatestRatesData(self):                   
        idx = len(self.sorteddata) - 1
        return self.load(idx)
    
    def getInitialRatesData(self):
        return self.load(0)
    
    def getPreviousData(self):        
        return self.load(len(self.sorteddata)-2)
    
    def load(self, idx):
        if  idx > -1 and idx < len(self.sorteddata):
            return self.sorteddata[idx]
        return None
        
    def getRecordCount(self):
        return len(self.sorteddata)