file = open("textfile.txt")
for line in file:
    words = line.split()
    for word in words:
        print(word,end='#')
    print()
file.close()
