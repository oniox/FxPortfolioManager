'''
Created on 19 Jul 2014

@author: Franklin Nwankwo
'''

class RatesCalculator(object):
    '''
    Checks threshold
    '''
    THRESHOLD = 1/100.0


    def __init__(self):
        pass
    
    
    def getRatesAboveThreshold(self, originalRates, prevRates, latestRates):
        assert len(prevRates) == len(latestRates) == len(originalRates)
        assert prevRates.keys() == latestRates.keys() == originalRates.keys()        
        rates = [(k,prevRates[k], latestRates[k])  for k in latestRates.keys() 
                 if self.isAboveTheshold(originalRates[k], latestRates[k])]
        return rates
       
    def isAboveTheshold(self, oldValue, newValue):
        if oldValue == newValue or (newValue < oldValue):
            return False
        elif newValue > (oldValue + (oldValue * self.THRESHOLD)):
            return True
        else:
            return False
            
                                                     
        