import random

cons_fdict = {'x': 5, 'z': 5, 'k': 39, 'h': 305, 'r': 300, 'l': 200, 'p': 95, 't': 455, 'c': 140, 'd': 210, 'n': 338, 's': 320, 'w': 120, 'j': 7, 'y': 100, 'm': 120, 'g': 100, 'b': 75, 'q': 5, 'v': 45, 'f': 110}

cons = "".join(letter * cons_fdict[letter] for letter in cons_fdict)

vowels = "aaaeeeiiooue"

def genword(phrases=3):
	w = ""
	for i in range(phrases):
		if random.random()<0.05:
			w += random.choice(cons)
		w += random.choice(cons)
		w += random.choice(vowels)
	if random.random()<0.5:
		w += random.choice(cons)
	return w

def gentextbody(length=100):
	b = ""
	lastlen = 1
	runningwords = 0
	for w in range(length):
		tlen = int(max(random.normalvariate(3.0 - lastlen, 1), 1) + 0.5)
		word = genword(tlen)
		if runningwords==0:
			word = word[0].upper() + word[1:]
		lastlen = tlen
		runningwords += 1
		b += word
		if random.random() < (runningwords-7)/17.0:
			b += "."
			runningwords = 0
		elif random.random() < 0.1:
			b += ","
		b += " "
	return b


