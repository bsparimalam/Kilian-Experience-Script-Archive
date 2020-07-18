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

import os, glob, json, re
from difflib import SequenceMatcher

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
wordcloud = ''
files = fileobject.paths
filenames = fileobject.filenames

for i, filename in enumerate(filenames):
	try:
		parameters = filename.replace(fileobject.extension, "").replace("xcolonx", ":").replace("xquestionx", "?").replace("xfslashx", "/").split('xsplitx')
		episode = {}
		episode["date"] = parameters[0]
		wordcloud += f'{parameters[1]} '
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
				wordcloud += f'{classifiedlist[j]} '
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
		wordcloud += f'{parameters[1]} '
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
				wordcloud += f'{classifiedlist[j]} '
				texts['text'] = texts['text'][:len(texts['text'])-1]
				script.append(texts)
		episode["script"] = script
		jsonobject.append(episode)
	except:
		print(filename, rawtextitem)
		break

wordcloud = re.sub('[^A-Za-z0-9\s\']+', ' ', wordcloud).replace('  ', ' ').replace('  ', ' ')
wordlist = wordcloud.split(' ')
phrasefrequency = []
shortphraselen = 3
longphraselen = 8
progress = 0
for i in range(len(wordlist)-longphraselen):
	currentprogress = int(i*100/len(wordlist))
	if (currentprogress > progress):
		print(f'phrase frequency calculation, {currentprogress}% complete')
		progress = currentprogress
	for j in range(shortphraselen, longphraselen):
		phrase = ' '.join(wordlist[i:i+j])
		count = wordcloud.count(phrase)
		if (count > 4):
			phrasefrequency.append({
				'phrase': phrase, 
				'count': count*(len(phrase)**3)
			})
i=0
progress = 0
while ( i < len(phrasefrequency)):
	currentprogress = int(i*100/len(phrasefrequency))
	if (currentprogress > progress):
		print(f'duplication removal, {currentprogress}% complete')
		progress = currentprogress
	phrase = phrasefrequency[i]["phrase"]
	j = 0
	while ( j < len(phrasefrequency)):
		if (phrasefrequency[j]["phrase"].count(phrase) > 0):
			phrasefrequency.remove(phrasefrequency[i])
			if (j < i): i -= 1 
			break

		if (SequenceMatcher(None, phrase, phrasefrequency[j]["phrase"]).ratio() > 0.6):
			if (len(phrase) > len(phrasefrequency[j]["phrase"])):
				phrasefrequency.remove(phrasefrequency[j])
				if (j < 1): i -= 1
			else:
				phrasefrequency.remove(phrasefrequency[i])
				if(j < i): i -= 1
		j += 1
	i += 1

def getvalue(e): return e["count"]
phrasefrequency.sort(reverse=True, key=getvalue)
print(json.dumps(phrasefrequency))

# jsonobject = json.dumps(jsonobject)
# print(jsonobject)