import datetime

# open file
file1 = open("Text.txt")

# read content
read_content = file1.read()
print(read_content)

# close file
file1.close()


# open a new file
file2 = open("Text2.txt", "w")
file2.write("This is a new file.\n")
file2.write("To be continued.\n")
file2.write(f"{datetime.datetime.now()}")

# close file
file2.close()

# this apporach closes the file authomatically
with open("Text.txt", "r") as file1:
    read_content = file1.read()
    print(read_content)

