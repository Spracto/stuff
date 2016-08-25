students = [
    {'first_name' : 'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

nlist = []
fname = []
lname = []

for x in students:
    for val in x.items():
        nlist.append(val)

for x in nlist:
    fname = x[0][0]
    lname = x[:1]

print fname
