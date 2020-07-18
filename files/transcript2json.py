# # AIzaSyDpeAqSvdqzohEewoZh_FslkTKVQKQmJgU apikey
# # UUjdQaSJCYS4o2eG93MvIwqg uploadsId
# # UCjdQaSJCYS4o2eG93MvIwqg channelId
# import requests, json

# response = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?playlistId=UUjdQaSJCYS4o2eG93MvIwqg&key=AIzaSyDpeAqSvdqzohEewoZh_FslkTKVQKQmJgU&maxResults=1&part=snippet")
# a = json.loads(response.text)
# print(response.text)

# response = requests.get("https://www.googleapis.com/youtube/v3/caption/id=i1MXYDkXZAE&key=AIzaSyDpeAqSvdqzohEewoZh_FslkTKVQKQmJgU")
# a = json.loads(response.text)
# print(response)

import os, glob, json

def timerange2stamp(string):
	rangelist = string.split(',')
	timelist = rangelist[0].split(':')
	return 3600*int(timelist[0]) + 60*int(timelist[1]) + int(float(timelist[2]))

class Files:
	def __init__(self, path):
		self.path = path
		self.extension = path[path.rindex('.'):]
		# try:
		self.filename = path[path.rindex('/')+1:]
		self.folder = path[:path.rindex('/')+1]
		self.paths = sorted(glob.glob(f"{self.folder}*{self.extension}"))
		self.filenames = [path[path.rindex('\\')+1:] for path in self.paths]

fileobject = Files('F:/Downloads/kilian-experience/files/complete scripts/*.sbv')
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

fileobject = Files('F:/Downloads/kilian-experience/files/incomplete scripts/*.sbv')
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

jsonobject = json.dumps(jsonobject)
print(jsonobject)