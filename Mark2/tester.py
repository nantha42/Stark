import threading
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.corpus import brown
from nltk.tag import pos_tag
import json
import time
import networkx as nx
from networkx.readwrite import json_graph

class Lang(threading.Thread):
	def __init__(self):
		self.W = None
		jfile = json.loads(open("Weather_network.json",'r').read())
		self.W = json_graph.jit_graph(jfile)

		pass
	 
	def parser(self,req):
		tokens = word_tokenize(req)

	def database(self):
		
		while(1):
			Wwords = input("Input some weather words")
			j = word_tokenize(Wwords)

		pass
	def pattern(self):
		for sent in brown.sents()[1:10]:
			patt = []
			tag_sent = pos_tag(sent)
			#print(tag_sent)
			for word,tag in tag_sent:
				if tag in ['VBN','VBD','VBP']:
					patt.append(tag)
				elif tag in ['NN','NNP','NNS']:
					patt.append('__')
				else:
					patt.append(word)
			print(patt)





if __name__ == '__main__':
	l = Lang()
	l.pattern()
	
