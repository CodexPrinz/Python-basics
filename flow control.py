#### flow control ####
print("Flow control")
print("-- if else elif --")
#num = input("Enter a number: ")
#num = int(num)
num = 1

if num > 0:
    print("is positive", num)
elif num < 0:
    print("is negative", num)
else: 
    print("is zero", num)


print("-- for loop --")
languages = ["SWIFT", "PYTHON", "GO"]

for i in languages:
    print(i)

language = "PYTHON"
for x in language:
    print(x)

print(" Range ")
for a in range(4):
    print(a)

print("------------------------> WHILE <---------------------------")
number = 1
while number <= 3:
    print(number)
    number+=1

print("---------------> Break & Continue <--------------")
for i in range(5):
    if i == 3:
        break
    print(i)

# Program to print odd numbers from 1 to 10
print("------------------------------------------")
num = 0

while num < 10:
    num += 1
    
    if (num % 2) == 0:
        continue

    print(num)    

print("---------------> Python pass Statement <--------------") 

   