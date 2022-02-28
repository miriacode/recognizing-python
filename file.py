num1 = 42 #variable declaration, primitive, number
num2 = 2.3 #variable declaration
boolean = True #variable declaration, primitive, boolean
string = 'Hello World' #variable declaration, primitive, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']#composite, list, initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#composite, dictionary, initialize
fruit = ('blueberry', 'strawberry', 'banana')#composite, tuple, initialize
print(type(fruit)) #type check
print(pizza_toppings[1])#list, access value
pizza_toppings.append('Mushrooms') #list, add value
print(person['name'])#dictionary, access value
person['name'] = 'George' #dictionary, change value
person['eye_color'] = 'blue' #dictionary, change value
print(fruit[2]) #tuple, access value

if num1 > 45: #conditional if
    print("It's greater")
else: #conditional else
    print("It's lower")

if len(string) < 5: #length check, conditional if
    print("It's a short word!")
elif len(string) > 15: #length check, , conditional elif
    print("It's a long word!")
else: # conditional else
    print("Just right!")

for x in range(5): #for loop
    print(x)
for x in range(2,5): #for loop
    print(x)
for x in range(2,10,3): #for loop
    print(x)
x = 0
while(x < 5): #while loop
    print(x)
    x += 1 #increment

pizza_toppings.pop() #list, delete value
pizza_toppings.pop(1) #list, delete value

print(person)
person.pop('eye_color') #KeyError: 'eye_color'
print(person)

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #conditional if
        continue #continue
    print('After 1st if statement')
    if topping == 'Olives': #conditional if
        break #break

def print_hello_ten_times(): #function
    for num in range(10): #for loop
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x): #function, parameter
    for num in range(x): #for loop
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): #function, argument
    for num in range(x): #for loop
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


#Multiline comment
"""
Bonus section 
"""


#single line comments

# print(num3)                     #NameError: name <variable name> is not defined
# num3 = 72                       #variable declaration
# fruit[0] = 'cranberry'          #TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])  #KeyError: 'favorite_team'
# print(pizza_toppings[7])        #list index out of range
#   print(boolean)                #NameError: name <variable name> is not defined
# fruit.append('raspberry')       #AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)                    #AttributeError: 'tuple' object has no attribute 'pop'