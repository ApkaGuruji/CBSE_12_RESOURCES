import pickle

records = [
    {'roll':1,'name':'Suraj'},
    {'roll':2,'name':'Sanjay'},
    {'roll':3, 'name':'Ravi'},
    {'roll':4, 'name':'Krishna'}
    ]

file = open("file.dat",'wb')
for record in records:
    pickle.dump(record,file)
file.close()


roll = int(input("Enter the roll to search: "))
file = open("file.dat","rb")
result = None
while True:
    try:
        record = pickle.load(file)
        if roll == record['roll']:
            result = record
    except EOFError:
        break
file.close()
if result is None:
    print("Not found")
else:
    print("Name is: ", result['name'])
