# update values in dictionaries and lists 

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30

x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30


# Pt2

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary(some_list):
    for item in some_list:
        for key, value in item.items():
            print(f'{key} - {value}')

def iterateDictionary2(key_name, some_list):
    for item in some_list:
        print(item[key_name])

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f"{key} - {len(value)}")
        for item in value:
            print(item)


iterateDictionary(students)
print("\n")
iterateDictionary2('first_name', students)
print("\n")
iterateDictionary2('last_name', students)
print("\n")
printInfo(sports_directory)