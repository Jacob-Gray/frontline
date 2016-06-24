from chat import ChatBot
from api import Api
from question import Question
import re
import enchant

bot = ChatBot("stackoverflow.com").join("113461");
bot.send("FrontLine started")

dictionary = enchant.Dict("en_US")

def filterQuestions(results):
	global bot
	for x in results["items"]:
		englishWords = 0;
			
		question = Question(x)
		
		for y in question.body:
			if y.name == "p":
				paragraph = 0
				text = y.text.split(" ");
				# print "Paragraph ("+str(len(text))+") [",
				for word in text:
					stripped = re.sub(r'\W+', '', word)
					# print stripped,
					if len(stripped) > 0 and dictionary.check(stripped):
						englishWords += 1
						paragraph+=1
				# print "] ("+str(paragraph)+" of these are english words)"
			# elif y.name == "pre":
				# text = y.text.split("\n");
				# print "Code Block ("+str(len(text) - 1)+" Lines)"
		
		if englishWords < 40:
			bot.send("Potential low-quality question: ["+question.title+"]("+question.link+")")
			
api = Api("stackoverflow")
api.questions(filterQuestions)
    


