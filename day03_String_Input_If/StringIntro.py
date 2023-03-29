word = 'Pyhton'
print(len(word))
print(word[2])
lenght = len(word)
lastChar = word[lenght - 1]
print(f'last character of {word} is {lastChar}')

sentence = 'I want to learn Python'
word2 = sentence[16:]
print(word2)
word2 = sentence[:15]
print(word2)

lowerSentence = sentence.lower()
print(lowerSentence)  # make it lower case

upperSentence = sentence.upper()
print(upperSentence)

name = ' joshua osin '
name = name.strip()  # remove whitespaces
print(name.capitalize())  # first char upper => Joshua osin
print(name.title())  # first char of each word=> Joshua Osin

print(name.index('o'))
print(name.rindex('o'))

index_number = sentence.index('P')
print(sentence[index_number:])

sentence = 'I love Java Programming Language'
print(sentence.replace('Java', 'Python'))

print(sentence.count('a'))

url = 'www.amazon.com'
boolean1 = url.startswith('www.')
print(boolean1)
