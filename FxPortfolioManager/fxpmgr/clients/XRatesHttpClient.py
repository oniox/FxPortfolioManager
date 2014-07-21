'''Created on 19 Jul 2014
@author: Franklin Nwankwo'''

import urllib2
import contextlib
from fxpmgr.utils.XRatesHtmlParser import XRatesHtmlParser

class XRatesHttpClient(object):
	'''
	Fetches html doc behind specified url, parses it into a dict
	'''
	
	x_url = None
	
	def __init__(self, xurl):
		self.x_url=xurl
		
	def getXRatesData(self):
		with contextlib.closing(urllib2.urlopen(self.x_url)) as response:
			html = response.read()
		parser = XRatesHtmlParser()
		data = parser.feed(html)
		parser.close()
		return data