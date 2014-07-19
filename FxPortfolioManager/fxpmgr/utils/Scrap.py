from utils.XRatesHtmlParser2 import XRatesHtmlParser2
import urllib2
 
def main():
    # instantiate the parser and fed it some HTML
    #filehtml = open("c:/Windows/Temp/rates.htm", 'r');
    #print filehtml
    response = urllib2.urlopen("http://www.x-rates.com/table/?from=GBP")
    html = response.read()
    #print html
    parser=  XRatesHtmlParser2()
    #parser.feed('<html><head><title>Test</title></head><body><h1>Parse me!</h1></body></html>')
    xratesData = parser.feed(html)
    print xratesData
                        
        
if __name__ == "__main__":
    main()