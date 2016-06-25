import re
import enchant

dictionary = enchant.Dict("en_US")

def FilterCodeElement(cls, el):
	codeMeta = {}
	
	codeMeta["lines"] = getLines(el)
    
def FilterTextElement(cls, el):
	textMeta = {}
	
	textMeta["words"] = getValidWordCount(el);
	textMeta["chars"] = len(getChars(el))
	
	textMeta["bold"] = getBold(el)
	textMeta["italic"] = getItalic(el)
	textMeta["case"] = getUpperCase(el)

	cls.text.append(textMeta)
	
    
def getPercentage(main, partial):
	full = len(main) if type(main) is str else main
	per = len(partial) if type(partial) is str else partial
	return 100/full*per
	
def getLines(el):
	return len(el.text.split("\n")) - 1
	
def getBold(el):
	return len(getImmediateText(el, ["strong", "b"]))
	
def getItalic(el):
	return len(getImmediateText(el, ["em", "i"]))

def getUpperCase(el):
	chars = getChars(el)
	Ucount = 0
	Lcount = 0
	for char in chars:
		if char.isupper():
			Ucount += 1
		else: Lcount +=1
	return {"upper":Ucount,"lower":Lcount}

def getChars(el):
	return list(re.sub(r"[^a-zA-Z]","", el.text));
	
def getImmediateText(el,loop = False):
	if not loop:
		return el.find(text=True, recursive=False)
	else:
		amount = ""
		for sel in loop:
			for item in el.find_all(sel):
				amount += item.find(text=True, recursive=False)
		return amount
		
def getValidWordCount(el):
	words = re.sub(r"[^a-zA-Z0-9' ]","", el.text).split(" ")
	count = 0
	for word in words:
		if len(word) > 0 and dictionary.check(word):
			count += 1
	return count
	