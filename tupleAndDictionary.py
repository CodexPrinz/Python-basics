print("\n------------> Set <----------------")
tuple_constructor = tuple(("Jack", "Maria", "David"))
print(tuple_constructor)

print("\ncheck if element is in tuple")
print ("Alice" in tuple_constructor)
print("Jack" in tuple_constructor)

# create a set of integer type
print("\nSets: ")
student_id = {112,113,114,115,116}
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print("student ids: ",student_id)
print("vowel letters: ",vowel_letters)

# create an empty set
empty_set = set()
print("empty set: ",empty_set)
print("Type: ",type(empty_set))

languages = {'Swift', 'Java', 'Python'}
print('Initial Set:',languages)
# remove 'Java' from a set
removedValue = languages.discard('Java')
print('Set after remove():', languages)

# ------------> Dictionary <----------------
print("\n------------> Dictionary <----------------")
country_capital = {
    "USA": "DC",
    "India": "New Delhi",
    "UK": "London",
    "Germany": "Berlin"
}
print("Country Capitals: ",country_capital)
print("Type: ",type(country_capital))
print("\n")
for key, value in country_capital.items():
    print(key, ":", value)

print("\nCapital of Germany: ", country_capital["Germany"])
country_capital["France"] = "Paris"
print("\nCountry Capitals: ",country_capital)

print("\n--------------------------")
for country in country_capital:
    print(country, ":", country_capital[country])

print("\n length: ", len(country_capital))



