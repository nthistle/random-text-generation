import random

cons_fdict = {'x': 5, 'z': 5, 'k': 39, 'h': 305, 'r': 300, 'l': 200, 'p': 95, 't': 455, 'c': 140, 'd': 210, 'n': 338, 's': 320, 'w': 120, 'j': 7, 'y': 100, 'm': 120, 'g': 100, 'b': 75, 'q': 5, 'v': 45, 'f': 110}
# roughly relative frequency of consonants

cons = "".join(letter * cons_fdict[letter] for letter in cons_fdict)
# just puts them into a string I can call random.choice() on

vowels = "aaaeeeiiooue"
# rough guess of relative vowel frequency


# words always begin with consonants, have a 50/50 to end with vowel or consonant
# 5% chance to use 2 consonants instead of one each phrase, for no real reason
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


# most of these parameters are arbitrary, decided on sentence length between 7 and 24
# words, (scaling probability to end the sentence), which yields an average sentence
# length of 12.85 words. 10% chance to have a comma after any word that doesn't end the
# sentence. length of each word uses a min-capped normal distribution, parameterized
# inversely on the length of last word (longer words tend to be followed by shorter
# words, etc.)
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


