import csv

# Open the file
with open("results.csv", 'r') as file:
    # Read the file
    reader = csv.reader(file)
    # Print each row
    for row in reader:
        print(row)


# write to csv files
with open("write.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "Harry Potter", "Harry"])
    writer.writerow([2, "Lord of the Rings", "Frodo"])
    writer.writerow([3, "Star Wars", "Luke"])



# Writing Dictionaries to CSV Files
fieldnames = ["player", "team"]
with open("output.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"player": "Messi", "team": "Barcelona"})
    writer.writerow({"player": "Ronaldo", "team": "Juventus"})
    writer.writerow({"player": "Neymar", "team": "PSG"})

print("\nDone writing to csv file with name output.csv\n")
