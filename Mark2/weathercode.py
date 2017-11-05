import pandas as pd
import json
import urllib.request
import time

k = """{"coord":{"lon":79.72,"lat":12.83},"weather":[{"id":701,"main":"Mist","description":"mist","icon":"50n"}],"base":"stations","main":{"temp":301.15,"pressure":1007,"humidity":83,"temp_min":301.15,"temp_max":301.15},"visibility":4000,"wind":{"speed":2.6,"deg":300},"clouds":{"all":75},"dt":1507993200,"sys":{"type":1,"id":7834,"message":0.0061,"country":"IN","sunrise":1507941075,"sunset":1507983750},"id":1268159,"name":"Kanchipuram","cod":200}"""
def celcius(k):
	return (k-273.15)
	
def read_report():
	data = pd.read_csv('w_report.csv',sep = '|',names = ['time','json'])
	t = float(data['time'])
	k = data['json']
	
	if(time.time()-t<600):	
		jason = json.loads(k[0])
		jason = jason['list']
		#print(type(jason))
		for i in range(len(jason)):
			
			print("#####--Weather Report--#####")
			print("Time : %s"%(jason[i]['dt_txt']))
			print("Condition:%s"%(jason[i]['weather'][0]['description']))
			print("MaxT : %f C"%(celcius(jason[i]['main']['temp_max'])))
			print("MinT : %f C"%(celcius(jason[i]['main']['temp_min'])))
			print("\n\n")
		print(time.ctime())
			#print("Min Temperature:%f"%(celcius(jason[i]['main']['temp_min'])))
			#print("Humidity level :%f"%(jason[i]['main']['humidity']))
			#print("\n\nTime Left for another request:%s"%(time.ctime(time.time()+600-(time.time()-t))))
		#for key in jason['list'][0]:
		#for i in jason['list'][0].keys():
			#w = jason['list'][0]
			#print(w['main']['temp_min']-273,w['main']['temp_max']-273)
			
		
		#print(jason)
		return 1;
	else:
		return 0

csv = open("w_report.csv",'r').read()
key = "http://api.openweathermap.org/data/2.5/forecast?q=Kanchipuram&APPID=d500d89c5c31bf5d4e165dbaa8024895"
if csv == '':
	response =urllib.request.urlopen(key)
	sj = """%s"""%(response.read())
	data = sj[2:-1]
	dicat = json.loads(data)
	csv = open("w_report.csv",'w')
	csv.write(str(time.time())+'|'+sj[2:-1])
else:
	if(read_report()):
		pass
	else:
		print("New Request")
		response =urllib.request.urlopen(key)
		sj = """%s"""%(response.read())
		data = sj[2:-1]

		jason = json.loads(data)
		csv = open("w_report.csv",'w')
		csv.write(str(time.time())+'|'+sj[2:-1])



