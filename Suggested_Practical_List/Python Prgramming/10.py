import os
results = {}
email_folder = "emails"
file_names = os.listdir(email_folder)
for file_name in file_names:
    file_path = email_folder + "/" + file_name
    file = open(file_path)
    for line in file:
        words = line.split()
        for word in words:
            word = word.lower()
            wl = len(word)
            if wl>1 and word[wl-1] in '.?!,':
                word = word[0:wl-1]
            try:
                results[word] += 1
            except KeyError:
                results[word] = 1
    file.close()
mostcommon={'word':'','count':0}
print("Here are the complete list of words along with count: ")
print("word".ljust(20), "count".ljust(20))
for word in results:
    print(word.ljust(20), str(results[word]).ljust(20))
    if results[word]>mostcommon['count']:
        mostcommon['word']=word
        mostcommon['count']=results[word]
print("'{0}' is the most common word and occurs {1} times".format(mostcommon['word'],
      mostcommon['count']))

