file1 = open("file1.txt")
file2 = open("file2.txt","w")
for line in file1:
    if not ('a' in line):
        file2.write(line)
file1.close()
file2.close()
