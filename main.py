from utils.paperInfoGenerator import Generator
from utils.mongoDriver import Mongo
from utils.stdlibCrawler import Crawler

from modules.science import Science


yearMax = 2015
yearMin = 2005

def buildModuleMap():
  output = {} 
  science  = Science()
  output['Science']       = science
  return output
  

#map string of journal name to journal module (build a pool of module objects)
moduleMap = buildModuleMap()

#instantite a crawler
crawler = Crawler()

#instantite a generator
generator = Generator()

# output link file for journals in the map, output to local file
for journal in moduleMap.keys():
  generator.generatePaperLink(journal, moduleMap[journal], crawler, yearMax, yearMin)
'''

# parse individual paper info, save to database 
for journal in moduleMap.keys():

  #instantite a mongo driver toward the journal
  mongo = Mongo(journal)
  generator.generatePaperInfo(journal, moduleMap[journal], crawler, mongo, yearMax, yearMin)

'''
