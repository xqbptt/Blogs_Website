import requests
from bs4 import BeautifulSoup

class scraper:
    def __init__(self, URL):
        self.URL = URL
        self.page = requests.get(URL)
        self.soup = BeautifulSoup(self.page.content,'html.parser')
        self.title = self.soup.find('head').find('title').text
        self.imgsrc = self.soup.find('img')['src']
        self.description = ""
        for meta in self.soup.find('head').find_all('meta'):
            try:
                if meta['name'] == 'description':
                    self.description = meta['content']
            except:
                self.description = "not available"
        
    def __str__(self):
        return "Title: " + self.title + "\nDescription: " + self.description + "\nimage: " + self.imgsrc
