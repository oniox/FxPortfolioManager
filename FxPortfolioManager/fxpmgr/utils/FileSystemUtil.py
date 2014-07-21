import os
import time
import datetime
import json
from fxpmgr.utils import ConfigUtil

'''
    Persists and loads xrates data (persisted to  files, read as dict from files)
'''

inputDir = ConfigUtil.getFileDirectory()
if not os.path.exists(inputDir):
    os.makedirs(inputDir)
filenamePrefix = 'xrates'

tokenSep = '_'
timeformat = '%d%m%y%H%M%S'



def getSortedData():
    sorted_data = []
    for filename in getSortedFileNames():
        sorted_data.append(loadDictFromFile(filename))
    return sorted_data
        

def getSortedFileNames():
    filenames = getFileNames()
    dtFileDict = [ (getAsDate(f.split(tokenSep)[1]), f) for f in filenames ]
    ''' sort in asc order by date as parsed from string into tuple above '''
    sorted(dtFileDict, key=lambda tup: tup[0]);
    return [ tup[1] for tup in dtFileDict ]
    
def getFileNames():
    files = os.listdir(inputDir)
    return [f for f in files if os.path.isfile(os.path.join(inputDir, f)) and f.startswith(filenamePrefix)]

def getAsDate(strdt):
    return time.strptime(strdt, timeformat)
  

def writeDictToFile(data):
    filename = makeFileName()
    json.dump(data, open(os.path.join(inputDir, filename),'w'))
    
def loadDictFromFile(filename):
    #print filename
    return json.load(open(os.path.join(inputDir, filename)))
  
def makeFileName():
    timeToken = datetime.datetime.today().strftime(timeformat) 
    return filenamePrefix + tokenSep + timeToken  



