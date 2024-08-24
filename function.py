print("--------------------> Function <--------------------")
#def greet(name="User"):
 #   print("Good Morning "+name)

def add(a=1,b=2):
    return int(a)+int(b)

#greet("Usher")
#print("\nSunm: ",add(2,3))

#print("\n Sunm: ",add(input("Enter first value: "),input("Enter second value: ")))
print("\n Default sum: ",add())

#--------------------->Using *args and **kwargs in Functions<---------------------
print("\n\n--------------------->Using *args and **kwargs in Functions<---------------------")

def add_all(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

answer = add_all(1,2,3,4,5,6,7,8,9,10)
print("\n Sum of all: ",answer)


def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} is {value}")

greet(name="Usher", age=25, city="Lagos")

#------------------------------------------ Global --------------------------------------------------------
c = 8 # Global variable
def add_2():
    global c
    c = 0
    print("\nC: ",c)
    c = c + 2 
a = add_2()
print(a)
