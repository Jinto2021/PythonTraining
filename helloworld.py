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
