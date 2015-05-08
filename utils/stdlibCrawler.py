import urllib2, cookielib, httplib

class Crawler:
  def __init__(self):
    cookie_support= urllib2.HTTPCookieProcessor(cookielib.CookieJar())
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

  def crawl(self, url):
    try:
      response = urllib2.urlopen(url, timeout=120)
    except urllib2.HTTPError as e:
      print "url open exception: ", e.code
      return self.urllibread(url) 
    try:
      content = response.read()
    except httplib.IncompleteRead as e:
      print "web content read exception: ", e.code
      return self.urllibread(url) 
    return content
    
    
  

