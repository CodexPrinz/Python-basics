import random
import math

print("\n---------------> TYPES <--------------")
num1 = 5
print(num1, 'is of type', type(num1))

num2 = 5.42
print(num2, 'is of type', type(num2))

num3 = 8+2j
print(num3, 'is of type', type(num3))

print("\n---------------> TYPES <--------------")
print(0b1101011)  # prints 107
print(0xFB + 0b10)  # prints 253
print(0o15)  # prints 13

# Type Conversion in Python
num4 = complex('3+5j')
print(num4)  

print("\n---------------> Python Random Module <--------------")
print(random.randrange(10, 20))
list1 = ['a','b', 'c', 'd', 'e']
print(random.choice(list1))

random.shuffle(list1)
print(list1)
print(random.random())


print("\n---------------> Trig <--------------")
print(math.pi)
print(math.cos(math.pi))
print(math.exp(10))
print(math.log10(1000))
print(math.sinh(1))
print(math.factorial(6))