# dictionary
# xsplitx
# xcolonx
# xquestionx
# xfslashx


import os, glob, json, re
from difflib import SequenceMatcher

def timerange2stamp(string):
	rangelist = string.split(',')
	timelist = rangelist[0].split(':')
	return 3600*int(timelist[0]) + 60*int(timelist[1]) + int(float(timelist[2]))

def time2stamp(string):
	timelist = string.split(':')
	return 60*int(timelist[0]) + int(timelist[1])
class Files:
	def __init__(self, path):
		self.path = path
		self.extension = path[path.rindex('.'):]
		# try:
		self.filename = path[path.rindex('/')+1:]
		self.folder = path[:path.rindex('/')+1]
		self.paths = sorted(glob.glob(f"{self.folder}*{self.extension}"))
		self.filenames = [path[path.rindex('\\')+1:] for path in self.paths]

# Old Complete Scripts
fileobject = Files('complete scripts/*.sbv')
jsonobject = []
files = fileobject.paths
filenames = fileobject.filenames

for i, filename in enumerate(filenames):
	try:
		parameters = filename.replace(fileobject.extension, "").replace("xcolonx", ":").replace("xquestionx", "?").replace("xfslashx", "/").split('xsplitx')
		episode = {}
		episode["date"] = parameters[0]
		episode["title"] = parameters[1]
		episode["id"] = parameters[2]
		script = []
		# rawtext = codecs.open(files[i], "r", "utf-8")
		rawtext = open(files[i], "r")
		rawtext = rawtext.read()
		rawtextlist = rawtext.split('\n\n')
		for rawtextitem in rawtextlist:
			texts = {}
			classifiedlist = rawtextitem.split('\n')
			texts['timestamp'] = timerange2stamp(classifiedlist[0])
			texts['text'] = ''
			for j in range(1, len(classifiedlist)):
				texts['text'] = texts['text'] + classifiedlist[j] + " "
				texts['text'] = texts['text'][:len(texts['text'])-1]
				script.append(texts)
		episode["script"] = script
		jsonobject.append(episode)
	except:
		print(filename, rawtextitem)
		break

# New Complete Scripts
fileobject = Files('new scripts/*.txt')
files = fileobject.paths
filenames = fileobject.filenames

for i, filename in enumerate(filenames):
	try:
		parameters = filename.replace(fileobject.extension, "").replace("xcolonx", ":").replace("xquestionx", "?").replace("xfslashx", "/").split('xsplitx')
		episode = {}
		episode["date"] = parameters[0]
		episode["title"] = parameters[1]
		episode["id"] = parameters[2]
		script = []
		# rawtext = codecs.open(files[i], "r", "utf-8")
		rawtext = open(files[i], "r")
		rawtext = rawtext.read()
		rawtextlist = rawtext.split('\n')
		aggregate = 4
		scriptlen = len(rawtextlist)//(aggregate*2)
		for j in range(0, len(rawtextlist), aggregate*2):
			texts = {}
			texts['timestamp'] = time2stamp(rawtextlist[j])
			texts['text'] = ''
			for k in range(j+1, min(j+aggregate*2, len(rawtextlist)-1), 2):
					texts['text'] = texts['text'] + " " + rawtextlist[k]
			script.append(texts)
		episode['script'] = script
		jsonobject.append(episode)
	except:
		print(filename, i, j, k, script)
		break

#Incomplete Scripts
fileobject = Files('incomplete scripts/*.sbv')
files = fileobject.paths
filenames = fileobject.filenames

for i, filename in enumerate(filenames):
	try:
		parameters = filename.replace(fileobject.extension, "").replace("xcolonx", ":").replace("xquestionx", "?").replace("xfslashx", "/").split('xsplitx')
		episode = {}
		episode["date"] = parameters[0]
		episode["title"] = parameters[1] + ' [transcription incomplete]'
		episode["id"] = parameters[2]
		script = []
		rawtext = open(files[i], "r")
		rawtext = rawtext.read()
		rawtextlist = rawtext.split('\n\n')
		for rawtextitem in rawtextlist:
			texts = {}
			classifiedlist = rawtextitem.split('\n')
			texts['timestamp'] = timerange2stamp(classifiedlist[0])
			texts['text'] = ''
			for j in range(1, len(classifiedlist)):
				texts['text'] = texts['text'] + classifiedlist[j] + " "
				texts['text'] = texts['text'][:len(texts['text'])-1]
				script.append(texts)
		episode["script"] = script
		jsonobject.append(episode)
	except:
		print(filename, rawtextitem)
		break

jsonobject = json.dumps({"scripts": jsonobject})

file = open('source.json', "w")
file.write(jsonobject)
file.close()