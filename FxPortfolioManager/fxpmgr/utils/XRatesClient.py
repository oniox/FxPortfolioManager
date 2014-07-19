'''Created on 19 Jul 2014
@author: Franklin Nwankwo'''

from utils.XRatesHtmlParser2 import XRatesHtmlParser2
import urllib2
import contextlib

class XRatesHttpClient(object):
	
	xURL = None
	
	def __init__(self, xURL):
		self.xURL=xURL
		
	def getXRatesData(self):
		with contextlib.closing(urllib2.urlopen(self.xURL)) as response:
			html  = response.read()
		parser = XRatesHtmlParser2()
		return parser.feed(html)