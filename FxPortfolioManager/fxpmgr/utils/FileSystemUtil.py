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

def sortFileNames(filenames):
    dtFileDict = [ (getAsDate(f.split(tokenSep)[1]), f) for f in filenames ]
    print dtFileDict
    # sort by date as parsed from string into tuple above
    return sorted(dtFileDict, key=lambda tup: tup[0]);
    
def getAsDate(strdt):
    return time.strptime(strdt, timeformat)
  

def writeDictToFile(data):
    filename = makeFileName()
    json.dump(data, open(os.path.join(inputDir, filename),'w'))
    
def loadDictFromFile(filename):
    return json.load(open(os.path.join(inputDir, filename)))
  
def makeFileName():
    timeToken = datetime.datetime.today().strftime(timeformat) 
    print timeToken
    return filenamePrefix + tokenSep + timeToken  



