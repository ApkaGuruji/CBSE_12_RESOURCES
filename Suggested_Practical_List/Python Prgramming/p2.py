file = open("textfile.txt")
data = file.read()
vowels = 0
consonants = 0
capital = 0
small = 0
for ch in data:
    if ch.isalpha():
        if ch.lower() in 'aeiou':
            vowels += 1
        else:
            consonants += 1
        if ch.isupper():
            capital += 1
        elif ch.islower():
            small += 1
file.close()
print(vowels , 'vowels' , consonants,
      'consonants', capital , 'capital', small,'small')
    
