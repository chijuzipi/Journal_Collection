'''
**************************************************************************
*********** The class is to generate invidiual paper url link
  (c) 2015 by Chad Zhou
  Northwestern University
**************************************************************************
'''
import time, datetime
import re

class Generator:

  # a specific journal module is passed to constructor
  def __init__(self):
    print "Generator constructed"

  def generatePaperLink(self, journal, jModule, crawler, yearMax, yearMin):
    inFile   = "archive/" + journal + "_issue.txt"
    outFile  = "archive/" + journal + ".txt"
    fIn         = open(inFile, 'r')
    fOut        = open(outFile, 'w')
    pool = fIn.readlines()

    for url in pool:
      urlDivid  = url.split() 
      url  = urlDivid[0]
      year = urlDivid[1]
      if int(year) >= yearMin and int(year) <= yearMax:
        print "CRAWLING: " + year  + " " + url
        print datetime.datetime.now()
        content = crawler.crawl(url)
        paperLinks = jModule.parsePaperLinks(content, journal)
        for link in paperLinks:
          fOut.write("http://www.sciencemag.org" + link + " " + year + '\n')

  def generatePaperInfo(self, journal, jModule, crawler, mongo, yearMax, yearMin):
    inFile   = "archive/" + journal + ".txt"
    fIn         = open(inFile, 'r')
    pool = fIn.readlines()

    interval = len(pool)/20
    index = 0

    while index != len(pool):
      url = pool[index]
      urlDivid  = url.split() 
      url  = urlDivid[0]
      year = urlDivid[1]
      if int(year) >= yearMin and int(year) <= yearMax:
        print "CRAWLING: " + year  + " " + url
        print datetime.datetime.now()
        content = crawler.crawl(url)
        paperInfo = jModule.parsePaperInfos(content, journal)

        for info in paperInfo:
          info = self.clean(info)
          print info
        print "*****************"
        print 

      index += interval
        #print paperInfo

  def clean(self, text):
    output = re.compile(r'[\n\r\t]').sub(' ', text).strip()
    output = re.sub(' +',' ', output)
    return output
    
    
