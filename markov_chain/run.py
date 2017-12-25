"""This is a python chat bot"""

class Response(object):
	def __init__(self,inp):
		self.input = inp
		self.answer = ""
	def reading(self,f):
		dic = {}
		
		with open(f,"r+") as db:
			i = 0
			for line in db:
				dic2 = {}
				split_line = db.split(",")
				for i in range(1,len(split_line),2):
					dic2[split_line[i]] = split_line[i+1]
				dic[0] = dic2
				i += 1
		return dic
	def __repr__(self):
		print dic

response = Response("")
db = response.reading("text.txt")
print db