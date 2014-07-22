'''
Created on 19 Jul 2014

@author: Franklin Nwankwo
'''

class RatesCalculator(object):
    '''
     Evaluates a collection of rates data values against a pre-specified rates threshold
    '''
   
    def __init__(self, threshold):
        self.threshold = float(threshold)
    
    
    def getRatesAboveThreshold(self, originalRates, prevRates, latestRates):
        assert len(prevRates) == len(latestRates) == len(originalRates)
        assert prevRates.keys() == latestRates.keys() == originalRates.keys()        
        rates = [(k,prevRates[k], latestRates[k])  for k in latestRates.keys() 
                 if self.isAboveTheshold(originalRates[k], latestRates[k])]
        return rates
       
    def isAboveTheshold(self, oldValue, newValue):
        if oldValue == newValue or (newValue < oldValue):
            return False
        elif float(newValue) > float(oldValue) + (float(oldValue) * self.threshold):
            #print '%s greater than %f >> ' %( newValue, (float(oldValue) + (float(oldValue) * float(self.threshold))) )
            return True
        else:
            return False
            
                                                     
        