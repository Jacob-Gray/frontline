from bs4 import BeautifulSoup
import urllib2

class Question:
	def __init__(self, item):
		
		#Copy info from json
		self.link = item["link"]
		self.title = item["title"]
		self.owner = item["owner"]
		self.score = item["score"]
		self.tags = item["tags"]
		
		#Parse question
		self.html = BeautifulSoup(self.read(self.link))
		self.body = self.getBody()
		
		self.code = []
		self.text = []
		self.wordCount = 0
		
	def read(self, url):
		return urllib2.urlopen(url).read();
		
	def getBody(self):
		return self.find("div.question div.post-text")[0].findChildren()
		
	def find(self, query):
		currentEl = None
		selectors = query.split(" ")
		
		for i,selector in enumerate(selectors):
			
			select = selector.split(".")
			elClass = select[1] if len(select) >1 else ""
			
			if i == len(selectors)-1:
				currentEl = (currentEl if currentEl != None else self.html).find_all(select[0], {'class': elClass});
			else: currentEl = (currentEl if currentEl != None else self.html).find(select[0], {'class': elClass});
		
		return currentEl
