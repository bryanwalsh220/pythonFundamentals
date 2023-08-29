num1 = 42 #variable declaration
num2 = 2.3 #variable dec
boolean = True 
string = 'Hello World'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit)) #log statement
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms')
print(person['name']) #log statement
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2]) #log statement

if num1 > 45: #conditional
    print("It's greater") #statement
else: #conditional
    print("It's lower") #statement

if len(string) < 5:#conditional
    print("It's a short word!")
elif len(string) > 15:#conditional
    print("It's a long word!")
else:#conditional
    print("Just right!")#statement

for x in range(5):
    print(x)#statement
for x in range(2,5):
    print(x)#statement
for x in range(2,10,3):
    print(x)#statement
x = 0
while(x < 5):
    print(x)#statement
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person) #log statement
person.pop('eye_color')
print(person) #log statment 

for topping in pizza_toppings: #forloop start
    if topping == 'Pepperoni':#conditional
        continue
    print('After 1st if statement')#statement
    if topping == 'Olives':#conditional
        break #forloop break 

def print_hello_ten_times():
    for num in range(10):
        print('Hello')#statement

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')#statement

print_hello_x_times(4)#statement

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')#statement

print_hello_x_or_ten_times()#statement
print_hello_x_or_ten_times(4)#statement


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)