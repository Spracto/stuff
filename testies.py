students = [
    {'first_name' : 'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

fnames = []
lnames = []

for item in students:
    fnames.append(str(item["first_name"]))
    lnames.append(str(item["last_name"]))

sdic = zip(fnames, lnames)

studic = dict(sdic)

for key, value in studic.items():
    print key, value
