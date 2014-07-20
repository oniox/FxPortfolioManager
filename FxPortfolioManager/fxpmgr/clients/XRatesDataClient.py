'''
Created on 20 Jul 2014

@author: FN
'''
from fxpmgr.utils import FileSystemUtil

class XRatesDataClient(object):
    '''
    Persists and loads xrates data as stored in files
    '''

    sorted_filenames = []

    def __init__(self):       
        self.sorted_filenames = FileSystemUtil.getSortedFileNames()
    
    
    def getLatestRatesData(self):                   
        idx = len(self.sorted_filenames) - 1
        return self.load(idx)
    
    def getInitialRatesData(self):
        return self.load(0)
    
    def getPreviousData(self):        
        return self.load(len(self.sorted_filenames)-2)
    
    def load(self, idx):
        if  idx > -1 and idx < len(self.sorted_filenames):
            return self.loadRatesData(self.sorted_filenames[idx])
        return None
        
    def getRecordCount(self):
        return len(self.sorted_filenames)
     
    def persistRatesData(self, rdata):
        return FileSystemUtil.writeDictToFile(rdata)   
    
    def loadRatesData(self, filename):
        return FileSystemUtil.loadDictFromFile(filename)