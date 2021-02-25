# update .travis.yml file to run only in Python 3.9 or multiple versionss simultaneously.

print("Welcome Python programmer/ beginner!")

day = 24
month = 'February'
year= 2021

date_txt="Python training started on " + month + " {1}, {0}."
display_date=date_txt.format(year,day)
print(display_date)

# unpacking tuple - example


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# also using Asterix * (since there is not 5 vasriables)
# (green, *tropic, red) = fruits

# Asterix feature throws error in Python 2.7 (in versions upto 3.7)
(green, tropic,tropic2,tropic3, red) = fruits 

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

aaa= """
This is how the dictionary 'thisdict' was created.

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": {"red":6, "white":1, "blue":False}
}
"""

print(aaa)
print("\n")
print(thisdict)

