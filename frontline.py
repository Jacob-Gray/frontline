from chat import ChatBot
from api import Api
from question import Question
from filters import Filter


bot = ChatBot("stackoverflow.com").join("113461");
api = Api("stackoverflow")

#Just for testing purposes, will be moved to seperate class
def filterQuestions(results):
	global bot
	for x in results["items"]:
		englishWords = 0;
			
		question = Question(x)
		
		quality = Filter(question)
		
		quality.countWords()
		quality.countLines()
		
		if quality.code == 0:
			bot.send("[tag:low-quality] No code - ["+question.title+"]("+question.link+")")
		elif quality.words < 5:
			bot.send("[tag:low-quality] No words - ["+question.title+"]("+question.link+")")
		elif quality.words < 40:
			bot.send("[tag:low-quality] Score:"+str(quality.words)+" - ["+question.title+"]("+question.link+")")
			
bot.send("FrontLine started")
api.questions(filterQuestions)
    


