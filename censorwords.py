def censor_word_string(text,censor_words,symbol):
    for word in censor_words:
        text = text.replace(word,len(word)*symbol)
    return text
text1 = censor_word_string("The Tiger jumped in River.",["The","Tiger"],"*")
print(text1)
#extra puzzle
word = "you shall not pass!"
print(word[len(word):0:-1] == word[::-1])
print(word[len(word)-1:-len(word)-1:-1] == word[::-1])
print(word[::-2])
print(word[:0:-1])
for i in range(10,15,1): 
    print(i,end=', ') 