from bs4 import BeautifulSoup

class Science:
  # parse invidiual paper link from the issue page
  def parsePaperLinks(self, content, journal):
    output = []
    soup = BeautifulSoup(content)
    urls = soup.findAll(href=True)
    for url in urls:
      url = url['href']
      if self.isPaperLink(url):
        output.append(url) 
    return output

  # parse individual paper info from the single paper page
  def parsePaperInfos(self, content, journal):
    atype         = ''
    atitle        = ''
    authors       = ''
    affi          = ''
    doi           = ''
    abstract      = '' 
    output = []

    soup = BeautifulSoup(content)
    article_type = soup.find('ul', {'class':'subject-headings'})
    if article_type is not None:
      atype = article_type.text

    article_title = soup.find('h1', {'id':'article-title-1'})
    if article_title is not None:
      atitle = article_title.text

    article_authors = soup.find('ol', {'class':'contributor-list'})
    if article_authors is not None:
      authors = self.parseAuthors(article_authors) 

    article_affi = soup.find('ol', {'class':'affiliation-list'})
    if article_affi is not None:
      affi = self.parseAffi(article_affi)

    article_doi  = soup.find('span', {'class':'slug-doi'})
    if article_doi is not None:
      doi = article_doi.text

    article_abs  = soup.find('div', {'id':'abstract-1'})
    if article_abs is not None:
      abstract = article_abs.text

    output.append(atype)
    output.append(atitle)
    output.append(authors)
    output.append(affi)
    output.append(doi)
    output.append(abstract)
    return output

  def parseAuthors(self, authors):
    output = ''
    authorNames = authors.findAll('span', {'class':'name'})
    if len(authorNames) > 0:
      for item in authorNames:
        output += item.text + ', '
    return output

  def parseAffi(self, aff):
    output = ''
    affis = aff.findAll('li', {'class':'aff'})
    if len(affis) > 0:
      for item in affis:
        output += item.text + '$$'
    return output

  def isPaperLink(self, url):
    if '/content/' in url and '.abstract' in url and len(url) == 30:
      return True
    return False
