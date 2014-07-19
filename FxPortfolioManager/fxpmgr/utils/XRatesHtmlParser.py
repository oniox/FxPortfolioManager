'''
Created on 19 Jul 2014

@author: onioxbiz
'''
from htmllib import HTMLParser


class XRatesHtmlParser(HTMLParser):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''   
    
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag
        
    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag
        
    def handle_data(self, data):
        print "Encountered some data  :", data
