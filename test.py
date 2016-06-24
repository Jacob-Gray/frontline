from question import Question
import re
import enchant

dictionary = enchant.Dict("en_US")

url = "http://stackoverflow.com/questions/37956751/what-does-private-mapstring-string-params-new-hashmap-mean-in-java";

englishWords = 0;
		
question = Question(url)

for y in question.body:
	if y.name == "p":
		paragraph = 0
		text = y.text.split(" ");
		print "Paragraph ("+str(len(text))+") [",
		for word in text:
			stripped = re.sub(r'\W+', '', word)
			print stripped,
			if len(stripped) > 0 and dictionary.check(stripped):
				englishWords += 1
				paragraph+=1
		print "] ("+str(paragraph)+" of these are english words)"
	elif y.name == "pre":
		text = y.text.split("\n");
		print "Code Block ("+str(len(text) - 1)+" Lines)"

if englishWords < 40:
	print "Low Q!"