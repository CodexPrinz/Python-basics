# Python Operators
print(5*3)
print(4/2)
print(11//3)
print(4**3)
print(5%3)

# Python Comparison Operators
a = 8
b = 11
print(a > b)
print((a>=8) and (b>1))
print(not True)

# Identity operators in Python
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)

# Membership operators in Python
print("\nMembership operators in Python")
message = "Hello world"
dict1  = {1:"a", 2:"b"}
print("H" in message)
print("Hello" in message)
print(1 in dict1)
print("a" in dict1)

def bill_split(amount, friends):
    amount = (0.2 * amount) + amount
    return amount / friends

result = bill_split(100,5)
print(result)