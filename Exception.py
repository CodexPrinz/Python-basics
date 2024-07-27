print("\nException handling")
try:
    numerator = 10
    denominator = 0
    result = numerator/denominator
    print(result)
except ZeroDivisionError:
    print("Error: Denominator cannot be 0.")

#print(dir(locals()["__builtins__"]))
print("\n")
try: 
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)



