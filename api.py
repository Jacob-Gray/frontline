import requests
import threading
import time

class Api:
    def __init__(self, host, timer = 60):
        
        self.time = int(time.time())
        self.apis = []
        self.host = host
        self.timer = timer
        self.call()
        
    def questions(self, callback):
        apiCall = "https://api.stackexchange.com/2.2/questions?order=desc&sort=creation&site=" + self.host
        self.apis.append([apiCall, callback])
        
    def answers(self, callback):
        apiCall = "https://api.stackexchange.com/2.2/answers?order=desc&sort=creation&site=" + self.host
        self.apis.append([apiCall, callback])
        
    def call(self):

        for api in self.apis:
            
            apiUrl = api[0]+'&fromdate='+str(self.time)
            r = requests.get(apiUrl)
            
            print "Api call to " + apiUrl
            
            self.time = int(time.time())
            api[1](r.json())
        threading.Timer(self.timer, self.call).start();