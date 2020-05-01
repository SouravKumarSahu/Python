#Calculate the frequency of each identified unique word in the list - words and store the result in the dictionary word_frequency.
#Hint: Use dictionary comprehensions and count method of lists

#Try it online https://code.sololearn.com/c7c9CJ8Cqki8

# convert paragraph into a list of words

words = ['sourav','sahu','sourav','kumar','sahu','sourav','sourav','sahu','sahu','sourav','kumar']
word_frequency = {i:words.count(i) for i in words}
print(word_frequency)
