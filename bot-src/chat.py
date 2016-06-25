import private.login
import ChatExchange.chatexchange.client
import ChatExchange.chatexchange.events


class ChatBot:
	def __init__(self, host):
		self.host = host
		self.rooms = {}
		self.client = ChatExchange.chatexchange.client.Client(host)
		self.client.login(private.email, private.password)
		print "Logged in to " + host + " as "+ self.client._br.user_name
		
	def join(self, room_id):
		room = self.client.get_room(room_id)
		room.join()
		self.rooms[room_id] = room
		print "Joined room "+str(room.id)
		return self
		
	def send(self, message):
		for room in self.rooms:
			self.rooms[room].send_message(message)
		return self
		


