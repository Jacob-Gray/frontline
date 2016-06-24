import re
import enchant
import defineFilters as filters

class Filter:
	
	def __init__(self, question):
		self.question = question
		self.score = 0
		self.words = 0
		self.code = 0
		self.dictionary = enchant.Dict("en_US")
		
	def checkText(self):
		opinion = ["is the best site","site is best"]
    
	def countWords(self):
		for y in self.question.body:
			
			if(y.name in filters.textElements):
			
				text = y.text.split(" ");
				for word in text:
	
					if len(word) > 0 and self.dictionary.check(word):
						self.words += 1

    
	def countLines(self):
		for y in self.question.body:
			
			if(y.name in filters.codeElements):
			
				self.code += len(y.text.split("\n")) -1;
    