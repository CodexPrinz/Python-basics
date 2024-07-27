import example
print("\n--------------> Recursion <--------------")
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
    
x = input("Enter a number: ")
print('\n Factorial of ', x)
print(factorial(int(x)))


c = example.add(5, 6)
print("\n", c)

print(dir(example))
print("\n",__name__)