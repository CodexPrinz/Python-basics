# assert
a = 4
assert a < 5

# error
#assert a > 5, "The value of a is too small"


# break or continue
print("\n-----Break-----")
for i in range(1, 11):
    if i == 5:
        break
    print(i)

print("\n\n-----Continue------")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# lambda
print("\n----------- lambda ----------")
a = lambda x: x*2
for i in range(1,6):
    print(f"value: {i} function map: {a(i)}")

# nonlocal
print("\n--------nonlocal-----------")
def outer_function():
    c = 4
    def inner_function():
        nonlocal c
        c = 10
        print("Inner function: ", c)
    inner_function()
    print("Outer function: ", c)

outer_function()