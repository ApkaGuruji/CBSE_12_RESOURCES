import pickle

records = [
    {'roll':1,'name':'Suraj','marks':56},
    {'roll':2,'name':'Sanjay','marks':90},
    {'roll':3, 'name':'Ravi','marks':95},
    {'roll':4, 'name':'Krishna','marks':45}
    ]

file = open("file2.dat",'wb')
for record in records:
    pickle.dump(record,file)
file.close()


roll = int(input("Enter the roll to search: "))
file = open("file2.dat","rb")
records = []
found = False
while True:
    try:
        record = pickle.load(file)
        if record['roll'] == roll:
            found = True
            marks = int(input("Enter the new marks: "))
            record['marks']=marks
        records.append(record)
    except EOFError:
        break
file.close()

if not found:
    print("Specified roll number does not exist")
else:
    file = open("file2.dat","wb")
    for record in records:
        pickle.dump(record,file)
    file.close()
    print("Marks updated successfully")
