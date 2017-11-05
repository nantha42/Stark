import time
import json
import threading
import random
import pandas as pd
import networkx as nx
import  urllib.request
from Language import Language
import  matplotlib.pyplot	as plt

class Brain(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.datafile = open("w_report.csv",'r')
		self.key = "http://api.openweathermap.org/data/2.5/weather?q=Kanchipuram&APPID=d500d89c5c31bf5d4e165dbaa8024895"
		self.last_update = []
		self.L = Language()
		self.Structure = nx.Graph()
		self.Structure.add_edges_from([('weather','description'),('weather','haze'),('wind','deg'),('wind','speed'),('main','humidity'),('main','temp'),('main','pressure'),('main','temp_max'),('main','temp_min'),('obj','dt'),('obj','main'),('obj','weather'),('obj','wind')])
		self.Structure.add_edges_from([('sys','sunrise'),('sys','sunset'),('obj','sys'),('obj','visibility'),('obj','coord'),('obj','clouds'),('clouds','all'),('obj','name'),('weather','id'),('weather','main')])
		nx.draw_networkx(self.Structure,show_labels = True)
		#plt.show()
	def celcius(self,k):
		return (k-273.15)

	def update(self):
		response =urllib.request.urlopen(self.key)
		sj = """%s"""%(response.read())
		data = sj[2:-1]
		jason = json.loads(data)
		csv = open("w_report.csv",'w')
		csv.write(str(time.time())+'|'+sj[2:-1])
		ch = random.choice([1,2,3])

		if ch == 1:
			print("The Weather is Updated@ %s and the last update was at %s"%(time.ctime(),time.ctime(self.last_update[-1])))
		elif ch == 2:
			print("The Weather data is Updated sir @ %s and the last update was at %s"%(time.ctime(),time.ctime(self.last_update[-1])))
		else:
			print("Star Weather data is updated at %s and the last update was at %s"%(time.ctime(),time.ctime(self.last_update[-1])))

	def checknow(self):
		data = self.datafile.read()
		while(1):
			if data == '':
				print("data == '")
				self.update()
				
			else:
				if(self.whentoupdate()):
					pass
				else:
					self.update()

			time.sleep(100)

	def whentoupdate(self):
		data = pd.read_csv('w_report.csv',sep = '|',names = ['time','json'])
		t = float(data['time'])
		k = data['json']
		
		if len(self.last_update)>0:
			if t!=self.last_update[-1]:
				self.last_update.append(t)
		else:
			self.last_update.append(t)
			print("Last Update:",time.ctime(self.last_update[-1]))

		if(time.time()-t<2000):
			return 1;
		else:
			return 0
	def json_search(self,whattoshow):
		
		for entity in whattoshow:
			path = nx.dijkstra_path(self.Structure,'obj',entity)
			data = self.get_data(path)
			if entity == 'temp_max' or entity == 'temp_min':
				print("%s is"%(entity),data-273.15,"C")
			else:
				print("%s is"%(entity),data)

	def get_data(self,lista):
		data = pd.read_csv('w_report.csv',sep = '|',names = ['time','json'])
		t = float(data['time'])
		k = data['json'][0]
		
		json_d = json.loads(k)
		if len(lista)==3:
			if lista[1] == 'weather':
				return json_d[lista[1]][0][lista[2]]
			else:
				return json_d[lista[1]][lista[2]]
		if len(lista)==2:
			
			return json_d[lista[1]]



	def run(self):
		threading._start_new_thread(self.checknow,())
		while(1):
			whattoshow = self.L.Talk()
			self.json_search(whattoshow)



		pass
if __name__ == '__main__':
	Stark = Brain()
	Stark.start()
		