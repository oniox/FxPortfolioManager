import os
import time
import datetime
import json

inputDir = "../../data"
filenamePrefix = 'xrates'

tokenSep = '_'
timeformat = '%d%m%y%H%M%S'


def getFileNames():
    files = os.listdir(inputDir)
    return [f for f in files if os.path.isfile(os.path.join(inputDir, f)) and f.startswith(filenamePrefix)]

def getSortedFileNames():
    filenames = getFileNames()
    dtFileDict = [ (getAsDate(f.split(tokenSep)[1]), f) for f in filenames ]
    ''' sort in asc order by date as parsed from string into tuple above '''
    sorted(dtFileDict, key=lambda tup: tup[0]);
    return [ tup[1] for tup in dtFileDict ]
    
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



