import os, glob, json, re
from difflib import SequenceMatcher

# class Files:
# 	def __init__(self, path):
# 		self.path = path
# 		self.extension = path[path.rindex('.'):]
# 		# try:
# 		self.filename = path[path.rindex('/')+1:]
# 		self.folder = path[:path.rindex('/')+1]
# 		self.paths = sorted(glob.glob(f"{self.folder}*{self.extension}"))
# 		self.filenames = [path[path.rindex('\\')+1:] for path in self.paths]

# fileobject = Files('F:/Downloads/kilian-experience/files/complete scripts/*.sbv')
# jsonobject = []
# wordcloud = ''
# files = fileobject.paths
# filenames = fileobject.filenames

# for i, filename in enumerate(filenames):
# 	try:
# 		rawtext = open(files[i], "r")
# 		rawtext = rawtext.read()
# 		rawtextlist = rawtext.split('\n\n')
# 		for rawtextitem in rawtextlist:
# 			classifiedlist = rawtextitem.split('\n')
# 			for j in range(1, len(classifiedlist)):
# 				wordcloud += f'{classifiedlist[j]} '
# 	except:
# 		print(filename, rawtextitem)
# 		break

# fileobject = Files('F:/Downloads/kilian-experience/files/incomplete scripts/*.sbv')
# files = fileobject.paths
# filenames = fileobject.filenames

# for i, filename in enumerate(filenames):
# 	try:
# 		rawtext = open(files[i], "r")
# 		rawtext = rawtext.read()
# 		rawtextlist = rawtext.split('\n\n')
# 		for rawtextitem in rawtextlist:
# 			classifiedlist = rawtextitem.split('\n')
# 			for j in range(1, len(classifiedlist)):
# 				wordcloud += f'{classifiedlist[j]} '
# 	except:
# 		print(filename, rawtextitem)
# 		break
# # frequency calculation
# wordcloud = re.sub('[^A-Za-z0-9s\']+', ' ', wordcloud).replace('  ', ' ').replace('  ', ' ')
# wordlist = wordcloud.split(' ')
# phrasefrequency = []
# phraselist = []
# shortphraselen = 4
# longphraselen = 9
# progress = 0
# for i in range(len(wordlist)-longphraselen):
# 	currentprogress = int(i*100/len(wordlist))
# 	if (currentprogress > progress):
# 		print(f'phrase frequency calculation, {currentprogress}% complete')
# 		progress = currentprogress
# 	for j in range(shortphraselen, longphraselen):
# 		phrase = ' '.join(wordlist[i:i+j])
# 		try:
# 			phraselist.index(phrase)
# 		except:
# 			phraselist.append(phrase)
# 			count = wordcloud.count(phrase)
# 			if (count > 4):
# 				phrasefrequency.append({
# 					'phrase': phrase, 
# 					'count': count*(len(phrase)**3)
# 				})
# print(f'{phrasefrequency=}')
# # discard substrings
# i=0
# progress = 0
# while ( i < len(phrasefrequency)):
# 	currentprogress = int(i*100/len(phrasefrequency))
# 	if (currentprogress > progress + 5):
# 		print(f'substrings removal, {currentprogress}% complete')
# 		progress = currentprogress
# 	j = 0
# 	while ( j < len(phrasefrequency)):
# 		phrase = phrasefrequency[i]["phrase"]
# 		phrase2 = phrasefrequency[j]["phrase"]
# 		if ((phrase2.count(phrase) > 0) and (i != j)):
# 			print(f'{i=} {j=} {phrase2=} {phrase=} {len(phrasefrequency)=}')
# 			phrasefrequency[j]["count"] = phrasefrequency[j]["count"] + phrasefrequency[i]["count"]
# 			phrasefrequency.remove(phrasefrequency[i])
# 			i = i - 2
# 			break
# 		j += 1
# 	i += 1
# print(f'substrings discarded = {phrasefrequency}')
phrasefrequency = [{'phrase': 'You get to pick', 'count': 16875}, {'phrase': 'was going to be', 'count': 23625}, {'phrase': 'going to be a', 'count': 13182}, {'phrase': "I think it's because", 'count': 40000}, {'phrase': 'Now you might be', 'count': 28672}, {'phrase': "And that's the Kilian", 'count': 55566}, {'phrase': 'The game starts with', 'count': 72000}, {'phrase': "I'm going to be", 'count': 23625}, {'phrase': 'have something to do with the', 'count': 368398}, {'phrase': 'to go out and', 'count': 10985}, {'phrase': 'part of the game', 'count': 24576}, {'phrase': "if you're interested in", 'count': 97336}, {'phrase': 'you should probably check out another review', 'count': 2720540}, {'phrase': 'the game actually starts', 'count': 82944}, {'phrase': 'But there was a', 'count': 16875}, {'phrase': 'should probably check out another review and', 'count': 842185}, {'phrase': "that's the kilian experience", 'count': 109760}, {'phrase': 'a member of the', 'count': 16875}, {'phrase': 'find out that the', 'count': 24565}, {'phrase': "I don't know I", 'count': 16464}, {'phrase': 'you might be saying', 'count': 41154}, {'phrase': 'turn it into a', 'count': 13720}, {'phrase': 'a bunch of people', 'count': 24565}, {'phrase': 'a bit of a', 'count': 8000}, {'phrase': "you don't want to", 'count': 24565}, {'phrase': 'I kind of like', 'count': 13720}, {'phrase': 'if you want to', 'count': 30184}, {'phrase': 'is a game where you', 'count': 79121}, {'phrase': 'the leader of the', 'count': 29478}, {'phrase': 'just a bunch of', 'count': 16875}, {'phrase': 'you get to face', 'count': 20250}, {'phrase': 'is going to be', 'count': 19208}, {'phrase': "If you're interested in", 'count': 60835}, {'phrase': "Ryan 'No ' says the man in", 'count': 357730}, {'phrase': 'What do you mean', 'count': 32768}, {'phrase': 'all over the place', 'count': 40824}, {'phrase': 'used to be a', 'count': 10368}, {'phrase': 'a lot of money', 'count': 13720}, {'phrase': 'have to go to', 'count': 17576}, {'phrase': 'have to travel to', 'count': 24565}, {'phrase': 'I just want to', 'count': 13720}, {'phrase': 'get out of here', 'count': 16875}, {'phrase': 'in a video game', 'count': 16875}, {'phrase': 'a lot of people', 'count': 30375}, {'phrase': 'at the same time', 'count': 28672}, {'phrase': 'for the first time', 'count': 46656}, {'phrase': 'I want you to', 'count': 10985}, {'phrase': 'you are supposed to', 'count': 48013}, {'phrase': 'I have no idea what', 'count': 149279}, {'phrase': 'the start of the', 'count': 24576}, {'phrase': 'to the top of', 'count': 10985}, {'phrase': 'I have yet to', 'count': 10985}, {'phrase': 'a bunch of stuff', 'count': 24576}, {'phrase': 'and you have to', 'count': 16875}, {'phrase': 'going to have to', 'count': 28672}, {'phrase': 'To get to the', 'count': 17576}, {'phrase': "I don't have to", 'count': 30375}, {'phrase': 'check out another review And that', 'count': 640175}, {'phrase': 'And that is the Kilian Experience', 'count': 2349780}, {'phrase': 'Did you know that', 'count': 34391}, {'phrase': 'in the game And', 'count': 16875}, {'phrase': 'for a couple of', 'count': 16875}, {'phrase': 'to get out of', 'count': 15379}, {'phrase': 'to travel to the', 'count': 20480}, {'phrase': 'to go to the', 'count': 17280}, {'phrase': 'So they go to', 'count': 10985}, {'phrase': 'they go to the', 'count': 13720}, {'phrase': 'is supposed to be', 'count': 24565}, {'phrase': 'supposed to be a', 'count': 20480}, {'phrase': 'Then we get to', 'count': 16464}, {'phrase': 'we get to pick', 'count': 13720}, {'phrase': 'this is the only', 'count': 20480}, {'phrase': 'Then a bunch of', 'count': 20250}, {'phrase': 'was supposed to be', 'count': 34992}, {'phrase': 'could really use a', 'count': 29160}, {'phrase': "You don't have to", 'count': 24565}, {'phrase': "you don't have to", 'count': 29478}, {'phrase': 'and that is the Kilian', 'count': 86990}, {'phrase': 'a lot of time', 'count': 15379}, {'phrase': "I don't know what to", 'count': 123203}, {'phrase': 'in the first game', 'count': 24565}, {'phrase': 'I have decided to', 'count': 29478}, {'phrase': 'made it to the', 'count': 19208}, {'phrase': 'the end of the', 'count': 21952}, {'phrase': 'for the rest of', 'count': 16875}, {'phrase': 'I have to do', 'count': 10368}, {'phrase': 'in the middle of', 'count': 32768}, {'phrase': 'the rest of the', 'count': 33750}, {'phrase': 'I have no idea how', 'count': 83520}, {'phrase': 'have no idea how to', 'count': 50759}, {'phrase': 'I am going to', 'count': 39546}, {'phrase': 'that is the Killian Experience', 'count': 247420}, {'phrase': 'get to pick a', 'count': 10985}, {'phrase': 'the Pok mon League', 'count': 46656}, {'phrase': 'let me tell you', 'count': 33750}, {'phrase': 'has a lot of', 'count': 12096}, {'phrase': 'my game of the year', 'count': 153237}, {'phrase': 'game of the year because', 'count': 103415}, {'phrase': '10 out of 10', 'count': 8640}, {'phrase': 'Chrono Trigger OST 37 Delightful Spekkio', 'count': 866080}, {'phrase': 'I need to find', 'count': 16464}, {'phrase': 'in the Middle Ages', 'count': 40824}, {'phrase': 'would be able to', 'count': 20480}, {'phrase': 'teach you how to', 'count': 20480}, {'phrase': "so I'm going to", 'count': 16875}, {'phrase': "I don't know how", 'count': 24576}, {'phrase': "don't know how to", 'count': 34391}, {'phrase': "I don't know if", 'count': 16875}, {'phrase': 'in the real world', 'count': 24565}, {'phrase': 'like in real life', 'count': 24565}, {'phrase': 'The game begins with', 'count': 72000}, {'phrase': 'the Age of Fire', 'count': 27000}, {'phrase': "I don't want to be", 'count': 135260}, {'phrase': "I don't care about", 'count': 29160}, {'phrase': 'you play as a', 'count': 10985}, {'phrase': 'come up with a', 'count': 16464}, {'phrase': "I don't think he", 'count': 20480}, {'phrase': 'have a lot of', 'count': 13182}, {'phrase': 'We meet up with', 'count': 16875}, {'phrase': 'and the only thing', 'count': 34992}, {'phrase': "I'm going to show you how to", 'count': 787011}, {'phrase': "Today I'm going to", 'count': 34992}, {'phrase': "I don't have any", 'count': 84634}, {'phrase': 'game of all time', 'count': 32768}, {'phrase': "I didn't have a", 'count': 20250}, {'phrase': 'Game of the Year', 'count': 20480}, {'phrase': "I can't do it", 'count': 13182}, {'phrase': 'the only thing that', 'count': 34295}, {'phrase': 'only thing that can', 'count': 41154}, {'phrase': 'you know that the', 'count': 24565}, {'phrase': 'I have to get', 'count': 13182}, {'phrase': 'What do you want', 'count': 20480}, {'phrase': 'I have to go', 'count': 8640}, {'phrase': 'I just wanted to', 'count': 20480}, {'phrase': 'Harry Potter and the', 'count': 48000}, {'phrase': 'I would have to', 'count': 16875}, {'phrase': 'and I have a', 'count': 8640}, {'phrase': 'the link in the', 'count': 16875}, {'phrase': 'link in the top of the description', 'count': 805084}, {'phrase': 'transcription incomplete transcription incomplete', 'count': 823543}, {'phrase': 'incomplete transcription incomplete transcription', 'count': 588245}, {'phrase': 'poop poop poop poop poop poop', 'count': 259761}];
# discard close matches
i=0
progress = 0
while ( i < len(phrasefrequency)):
	# currentprogress = int(i*100/len(phrasefrequency))
	# if (currentprogress > progress + 5):
	# 	print(f'discarding close matches, {currentprogress}% complete')
	# 	progress = currentprogress
	j = 0
	while ( j < len(phrasefrequency)):
		phrase = phrasefrequency[i]["phrase"]
		phrase2 = phrasefrequency[j]["phrase"]
		if ((SequenceMatcher(None, phrase, phrase2).ratio() > 0.70) and (len(phrase) <= len(phrase2)) and (i != j)):
			# print(f'{i=} {j=} {phrase2=} {phrase=} {len(phrasefrequency)=}')
			phrasefrequency[j]["count"] = phrasefrequency[j]["count"] + phrasefrequency[i]["count"]
			phrasefrequency.remove(phrasefrequency[i])
			i = i - 1
			break
		j += 1
	i += 1
# print(f'close matches discarded = {phrasefrequency}')
cleanup = [
	"transcription incomplete transcription incomplete",
	"poop poop poop poop poop",
	"incomplete transcription incomplete transcription",
	"poop poop poop poop poop poop",
	"would be able to",
	"Chrono Trigger OST 37 Delightful Spekkio",
	"have something to do with the",
	"Ryan 'No' says the man in",
	"I don't care about",
	"all over the place",
"for the first time",
"you know that the", 
]
i=0
progress = 0
while ( i < len(phrasefrequency)):
	# currentprogress = int(i*100/len(phrasefrequency))
	# if (currentprogress > progress + 5):
	# 	print(f'cleanup, {currentprogress}% complete')
	# 	progress = currentprogress
	phrase = phrasefrequency[i]["phrase"]
	if (cleanup.count(phrase) > 0):
		phrasefrequency.remove(phrasefrequency[i])
		i = i - 2
	i += 1
# print(f'filtered = {phrasefrequency}')
def getsortparam(e): return len(e["phrase"])
phrasefrequency.sort(reverse=True, key=getsortparam)
print(f'{json.dumps(phrasefrequency)=}')
