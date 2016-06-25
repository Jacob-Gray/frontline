from chat import ChatBot
from api import Api
from question import Question
from filters import Filter
import json

#.join("113461")
bot = ChatBot("stackoverflow.com").join("68414");
api = Api("stackoverflow", 60)

#Just for testing purposes, will be moved to seperate class
def filterQuestions(results):
	global bot
	for x in results["items"]:
		englishWords = 0;
			
		question = Question(x)
		
		quality = Filter(question)
		quality.calc()
		print quality.score
		
		if quality.score < 40:
			message = ""
			for y in quality.text:
				message += "Words: `%i`, Chars: `%i`, Bold: `%i`, Italic: `%i`, Case=> Upper: `%i`, Lower: `%i`" % (y.get("words"), y.get("chars"), y.get("bold"), y.get("italic"), y.get("case").get("upper"), y.get("case").get("lower"))
			bot.send("[tag:low-quality] ["+question.title+"]("+question.link+") - "+message)


bot.send("FrontLine started")
api.questions(filterQuestions)

# question = Question({"link":"http://stackoverflow.com/questions/1881865/bold-labels-in-mfc"})
# quality = Filter(question)
# quality.calc()
# print json.dumps(quality.text, indent=4, sort_keys=True)


