'''Created on 19 Jul 2014
@author: Franklin Nwankwo'''

from utils.XRatesHtmlParser2 import XRatesHtmlParser2
import urllib2
import contextlib

class XRatesHttpClient(object):
	
	x_url = None
	
	def __init__(self, xurl):
		self.x_url=xurl
		
	def getXRatesData(self):
		with contextlib.closing(urllib2.urlopen(self.x_url)) as response:
			html = response.read()
		parser = XRatesHtmlParser2()
		data = parser.feed(html)
		parser.close()
		return data