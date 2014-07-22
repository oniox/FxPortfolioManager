'''

@author: FN
'''
import unittest
from fxpmgr.utils.XRatesHtmlParser import XRatesHtmlParser
from fxpmgr.utils.RatesCalculator import RatesCalculator
from fxpmgr.clients.XRatesDataClient import XRatesDataClient


class TestXRatesHtmlParser(unittest.TestCase):
    
    expratesData = {u'CNY/GBP': '0.094323', u'BGN/GBP': '0.404979', u'MXN/GBP': '0.045154', u'GBP/KZT': '313.082300', u'TTD/GBP': '0.091739', u'GBP/CLP': '964.472795', u'GBP/THB': '54.470336', u'INR/GBP': '0.009706', u'GBP/PHP': '73.970223', u'GBP/TWD': '51.275495', u'CAD/GBP': '0.545331', u'SAR/GBP': '0.156181', u'GBP/IRR': '44561.407061', u'LKR/GBP': '0.004496', u'CZK/GBP': '0.028831', u'PHP/GBP': '0.013519', u'ILS/GBP': '0.171355', u'KZT/GBP': '0.003194', u'GBP/NZD': '1.965585', u'GBP/BWP': '15.122530', u'NPR/GBP': '0.006040', u'GBP/TRY': '3.617081', u'HKD/GBP': '0.075559', u'GBP/ISK': '195.148150', u'GBP/LVL': '0.887302', u'GBP/RON': '5.617071', u'GBP/HUF': '390.730689', u'BND/GBP': '0.472573', u'GBP/KRW': '1752.688979', u'GBP/BGN': '2.469263', u'SEK/GBP': '0.085507', u'CLP/GBP': '0.001037', u'GBP/BRL': '3.793268', u'GBP/SAR': '6.402842', u'IDR/GBP': '0.000051', u'GBP/COP': '3178.201503', u'HUF/GBP': '0.002559', u'GBP/RUB': '60.067409', u'GBP/OMR': '0.657494', u'GBP/VEF': '10.743397', u'TRY/GBP': '0.276466', u'GBP/KWD': '0.481127', u'GBP/USD': '1.707334', u'OMR/GBP': '1.520926', u'EUR/GBP': '0.792064', u'MUR/GBP': '0.019017', u'LYD/GBP': '0.473376', u'GBP/NOK': '10.580610', u'BHD/GBP': '1.553192', u'DKK/GBP': '0.106238', u'GBP/MYR': '5.417369', u'NOK/GBP': '0.094513', u'PLN/GBP': '0.191030', u'GBP/AED': '6.271463', u'GBP/SEK': '11.694989', u'GBP/DKK': '9.412833', u'GBP/CAD': '1.833747', u'JPY/GBP': '0.005775', u'RON/GBP': '0.178029', u'GBP/PKR': '168.769924', u'KRW/GBP': '0.000571', u'LVL/GBP': '1.127012', u'GBP/HRK': '9.615184', u'GBP/HKD': '13.234738', u'TWD/GBP': '0.019502', u'IRR/GBP': '0.000022', u'VEF/GBP': '0.093080', u'GBP/CHF': '1.533353', u'GBP/MUR': '52.585874', u'RUB/GBP': '0.016648', u'USD/GBP': '0.585709', u'GBP/LYD': '2.112484', u'GBP/EUR': '1.262525', u'GBP/AUD': '1.821776', u'BRL/GBP': '0.263625', u'GBP/CNY': '10.601840', u'BWP/GBP': '0.066127', u'AUD/GBP': '0.548915', u'ARS/GBP': '0.071734', u'ZAR/GBP': '0.055217', u'ISK/GBP': '0.005124', u'CHF/GBP': '0.652166', u'GBP/QAR': '6.216402', u'COP/GBP': '0.000315', u'LTL/GBP': '0.229398', u'GBP/INR': '103.029046', u'KWD/GBP': '2.078455', u'GBP/MXN': '22.146673', u'GBP/LTL': '4.359245', u'GBP/CZK': '34.685285', u'GBP/SGD': '2.116076', u'GBP/ARS': '13.940379', u'GBP/IDR': '19753.854418', u'MYR/GBP': '0.184591', u'HRK/GBP': '0.104002', u'GBP/JPY': '173.157710', u'GBP/ZAR': '18.110461', u'GBP/BND': '2.116076', u'THB/GBP': '0.018359', u'GBP/PLN': '5.234778', u'QAR/GBP': '0.160865', u'AED/GBP': '0.159452', u'GBP/BHD': '0.643835', u'PKR/GBP': '0.005925', u'GBP/ILS': '5.835831', u'GBP/LKR': '222.422881', u'SGD/GBP': '0.472573', u'GBP/NPR': '165.572788', u'GBP/TTD': '10.900471', u'NZD/GBP': '0.508754'}

    def setUp(self):
        self.parser =XRatesHtmlParser()   

    def tearDown(self):
        pass


    def testRatesDataHTMLParsing(self):
        with open ('../../resources/xratescom_gbp.htm', 'r') as htmfile:
            xRatesHTML=htmfile.read()
        self.failUnless( self.parser.feed(xRatesHTML)==self.expratesData)


class TestRatesCalculator(unittest.TestCase):
    
    expovrthold = [('GBP/NOK', '10.5906', '10.7806'), ('GBP/USD', '1.7145', '1.7245')]
    ratescalc = RatesCalculator(0.01)
    
    def testIsAboveThreshold(self):
        self.failIf(self.ratescalc.isAboveTheshold(1.0,1.0))
        self.failUnless(self.ratescalc.isAboveTheshold(1.0,1.02))
    
    def testGetRatesAboveThreshold(self):
        ovrthold = self.ratescalc.getRatesAboveThreshold({'GBP/USD':'1.7045', 'GBP/JPY':'170.55','GBP/NOK': '10.5806'}, 
                                              {'GBP/USD':'1.7145', 'GBP/JPY':'169.55','GBP/NOK': '10.5906'}, 
                                              {'GBP/USD':'1.7245', 'GBP/JPY':'170.55','GBP/NOK': '10.7806'})
        self.failUnlessEqual(self.expovrthold, ovrthold)
        
class TestXRatesDataClient(unittest.TestCase):
    
    
    def testGetLatestData(self):
        dataclient = XRatesDataClient([])
        self.failUnless(dataclient.getInitialRatesData() == None and dataclient.getPreviousData() == None and dataclient.getLatestRatesData() == None)
        dataclient = XRatesDataClient(range(1))
        self.failUnless(dataclient.getInitialRatesData() == 0 and dataclient.getPreviousData() == None and dataclient.getLatestRatesData() ==0)
        dataclient = XRatesDataClient(range(3))
        self.failUnless(dataclient.getInitialRatesData() == 0 and dataclient.getPreviousData() == 1 and dataclient.getLatestRatesData() == 2)
    
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()