users = {
 'Students': [
     {'first_name' :  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

i = 1

for key, data in users.items():
    print key
    for value in data:
        x = value['first_name'] + value['last_name']
        print str(i) + " - " + value['first_name']+ " " + value['last_name'] + " - " + str(len(x))
        i = i + 1
