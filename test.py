# print a string
print("Hello world")
print('Hello world!')
# print a number
print(25)
# -------------
''' another form of comment '''
name = "John"
print(name)

# variables
num1 = 10
num2 = 30
sum = num1+num2
print("the sum is: ", sum)
# print("the product is: ", product)

site_name = "-- Learning python basics --"
print(site_name)

site_name = " change phrase"
print(site_name)

a,b,c,d = 12, '03', 50, 'ù'
print(a,b,c,d)

# Collections
fruits = ["apple", "mango", "orange"]
print(fruits)

# dictional literal
alphabets = {"a":"apple", "b":"ball", "c":"cat"}
print(alphabets)

# Type casting
integer_number = 125
float_number = 25.9
result = integer_number + float_number
print(result)
print("Data type: ",type(result))

print("integer: {}, float: {}".format(integer_number, float_number))
# user input
user_input = input("\nEnter any character: ")
print("You entered: {} of data type: {}".format(user_input, type(user_input)))

