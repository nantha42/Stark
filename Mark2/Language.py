import networkx as nx
from nltk import word_tokenize
from nltk.corpus import stopwords as sw
class Language:
	def __init__(self):
		self.W = nx.Graph()
		self.keywords = ['weather','humidity','temp_max','temp_min','wind','speed','pressure','deg','description','main','id','lat','lon','sunrise','sunset']
		self.keywords.extend(['visibility','all','clouds','name'])
		self.swords = sw.words('english')
		self.action_verbs = ['show','what','print','will']

		pass

	def request(self,data):
		weather_entity,verbs = data[1],data[2]

		actio_present = False
		for word in verbs:
			if word in self.action_verbs:
				actio_present = True;
				
				break;

		if actio_present == True:
			return weather_entity
		else:
			return []

	def Talk(self):
		inp = input(">>")
		inp_words = word_tokenize(inp)
		weather_entity = []
		verbs = []
		stopwords = []

		for w in inp_words:
			if w in self.keywords:
				weather_entity.append(w)
			elif w in self.swords:
				stopwords.append(w)
			else:
				verbs.append(w)
		
		data = self.request([stopwords,weather_entity,verbs])
		return data

if __name__ == '__main__':
	L = Language()
	