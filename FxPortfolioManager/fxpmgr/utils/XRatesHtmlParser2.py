
'''Created on 19 Jul 2014
@author: Franklin Nwankwo'''

from HTMLParser import HTMLParser


class XRatesHtmlParser2(HTMLParser):
    '''
        Contrived HTMl parser which scrapes rates data off data as fetched from x-rates.com.      
    '''
    isInTable = False
    isInTBody = False
    isInTRow = False
    isInAnchor=False
    currentAttrs = None
    fxPairDict = dict()
        
    def handle_starttag(self, tag, attrs):
        if not self.isInTable and tag == 'table':
            for k,v in attrs:
                if (k=='class' and  v=='ratesTable'):
                    self.isInTable = bool(1)
                    break
        elif self.isInTable:
            if self.isInTRow and tag == 'a':
                self.isInAnchor = True
                self.currentAttrs = attrs
            if tag == 'tbody':
                self.isInTBody = True
            #print tag
            if self.isInTBody and tag == 'tr':
                self.isInTRow = True
            
    def handle_endtag(self, tag):
        if self.isInTable and (tag == 'table' or tag == 'tbody'):
            self.isInTable,self.isInTBody = False,False
            print self.fxPairDict
            print "Encountered an end tag :", tag
        elif self.isInTBody and tag=='tr':
            self.isInTRow = False;            
        elif self.isInTRow and tag == 'a':
            self.currentAttrs = None
            self.isInAnchor = False
            
        
    def handle_data(self, data):
        if self.isInTRow and self.isInAnchor:
            key   =    self.currentAttrs[0][1].replace('&to=', '/')[13:20]
            value = data
            self.fxPairDict[key] = value
            
