import requests
import threading
import time
import enchant
import urllib2
import re
from bs4 import BeautifulSoup

dictionary = enchant.Dict("en_US")


currentTime = int(time.time())
def ping():
	global currentTime
	r = requests.get('https://api.stackexchange.com/2.2/questions?order=desc&sort=creation&site=stackoverflow&fromdate='+str(currentTime))
	currentTime = int(time.time())
	parse(r.json())
	threading.Timer(60, ping).start();
	
def parse(r):
	for x in r["items"]:
		url = x["link"]
		
		englishWords = 0
		html = urllib2.urlopen(url).read()
		soup = BeautifulSoup(html)
	
		questionParagraphs = soup.find('div', {'class' :'question'}).find("div",{"class":"post-text"}).find_all("p");

		for y in questionParagraphs:
			text = y.text.split(" ");
			for word in text:
			    
		
			    stripped = re.sub(r'\W+', '', word)
			    if len(stripped) > 0 and dictionary.check(stripped):
					englishWords+=1
					
		if englishWords < 40:
			print "We only found "+str(englishWords)+" english words in this question"
			print url
		

# start calling f now and every 60 sec thereafter
ping()