import urllib2
from bs4 import BeautifulSoup

def get_content(url):
    html = urllib2.urlopen(url)
    return BeautifulSoup(html,"lxml")

def extract(soup):

    print soup.title





soup = get_content("http://www.politico.com/2016-election/results/map/president/california/")
extract(soup)