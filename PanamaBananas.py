word = input('Enter a word: ')
suffixList = []

index = 0
for i in word:
	suffixList.append(word + ' ' + str(index))
	#cut the first char
	word = word[1 : : ]
	index += 1
	
suffixList.sort()
for x in range(len(suffixList)): 
    print(suffixList[x]) 
	
	
