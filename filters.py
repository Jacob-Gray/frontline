import defineFilters as filters

textElements = ["ul","p","h1","h2","h3","blockquote"]
codeElements = ["pre", "code"]

class Filter:
	def __init__(self, question):
		self.imgCount = 0
		self.score = 0
		self.code = []
		self.text = []
		for el in question.body:
			FilterElement(self, el)
			
	def calc(self):
		for item in self.text:
			self.score += item.get("words")
		

def FilterElement(self, el):
	if el.name in textElements:
		filters.FilterTextElement(self, el)
	elif el.name in codeElements:
		filters.FilterCodeElement(self, el)
	elif el.name == "img": self.imgCount +=1
		

    