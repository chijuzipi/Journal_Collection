from bs4 import BeautifulSoup

class ACS:
  def __init__(self):
    self.prefixMap = self.buildPrefixMap()

  def parseLink(self, content, journal):
    output = []
    soup = BeautifulSoup(content)
    urls = soup.findAll(href=True)
    for url in urls:
      url = url['href'].text
      if self.prefixMap[journal] in url:
        output.append(url) 

    return output

  def buildPrefixMap(self):
    output = {}
    output['JACS'] = 'http://pubs.acs.org/doi/abs/'
    output['NanoLetters'] = 'http://pubs.acs.org/doi/abs/'

    return output
