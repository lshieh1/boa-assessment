import operator

upperlimit = raw_input("Input upperlimit: ")
lowerlimit = raw_input("Input lowerlimit: ")

file = open("article.txt","r")
word_count = {}
for line in file:
	words = line.split(" ")
	for word in words:
		word = word.replace(".","")
		word = word.replace(",","")
		word = word.replace("\xe2\x80\x99","'")
		word = word.replace("\xe2\x80\x9d","")
		word = word.replace("\xe2\x80\x9c","")
		word = word.replace("\n","")
		if(word != '\xe2\x80\x94'):
			word = word.lower()
			if word not in word_count:
				word_count[word] = 0
			word_count[word] += 1

sorted_words = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)
for el in sorted_words:
	if(el[1] <= int(upperlimit) and el[1] >= int(lowerlimit)):
		print el[0], el[1]
