print("Welcome Python programmer/ beginner!")

day = 24
month = 'February'
year= 2021

date_txt="Python training started on " + month + " {1}, {0}."
display_date=date_txt.format(year,day)
print(display_date)

# unpacking tuple - example
# also using Asterix * (since there is not 5 vasriables)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#Dictionaries are ordered in python 3.7 and later.
print("Dictionaries are ordered in python 3.7 and later.\n")
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964.03,
  "colors": {"red":6, "white":1, "blue":False}
}

print("Printing once:\n")
print(thisdict)
print("Printing once:\n")
print(thisdict)
