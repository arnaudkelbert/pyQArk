import unittest
from pyQArk.Core import QArkDomXml

class QArkDomXmlTest(unittest.TestCase):
    """
    Test
    """
    def test_widget(self):
        s='<root><elt>0</elt><elt>1</elt></root>'
        print(QArkDomXml.toPrettyXmlString(s))

if __name__ == '__main__':
    unittest.main()