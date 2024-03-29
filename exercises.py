# Exercise 0
# Lists
fav_colors = ["Truqoise", "Electric Orange", "Cool blue", "Navy", "Yellow"]
ages = [25, 31, 24, 23, 22, 26]
coin_flips = [True, False, True, True, False] # True indicating that it was heads
fav_artists = ["Post Malone", "Billie Eilish", "Joji"]

# Dictionaries
words = {"Sardonic" : "Mocking and Cynical", "Contingency" : "Preparing for unforseen circumstance", "Peruse" : "Read thoroughly"}
fav_movies = {"Terminator 2" : 1991, "Lala Land" : 2016, "Spiderman Into the Spiderverse" : 2018}
cities = {"Hong Kong" : 7392000, "Toronto" : 2930000, "New York" : 8623000}
family_and_freinds = {"Sharon" : 31, "Moo Moo" : 22, "Aj" : 24, "Ian" : 24, "Keefe" : 42, "Kat" : 40}

#########################
# Exercise 1

# 1.1
for coin in coin_flips:
    print(coin)

# 1.2
print(fav_colors[0])

# 1.3
ages.sort() # sort does not return a value, thats why print(age.sort() doesn't work)
print(ages)

# 1.4
ages.append(0)
print(ages)

# 1.5
print(fav_movies["Terminator 2"])

###########################
# Exercise 2

# 2.1
print(fav_colors[-1])

# 2.2
cities["San Francisco"] = 884363
# Checking to see if it was added successfully
for city, pop in cities.items():
    print(f"{city} has a population of {pop}")

# 2.3
coin_flips.reverse() # Don't need to call to variable, reverse() just reverses and saves the variable
print(coin_flips) # Checking to see if it was reversed

# 2.4
print(cities["Hong Kong"])

# 2.5
for artist in fav_artists:
    print(f"I think {artist} is great")

############################
# Exercise 3

# 3.1
print(fav_artists[0:2])

# 3.2
for movie, year in fav_movies.items():
    print(f"{movie} came out {year}")

# 3.3
ages = sorted(ages, reverse = False)
print(ages)

# 3.4
fav_movies["Beauty and the Beast"] = [1991, 2017]
print(fav_movies["Beauty and the Beast"])

##############################
# Exercise 4

# 4.1
under_30 = list(filter(lambda age: age < 30, ages))
print(under_30)

# 4.2
print(max(ages))

# 4.3
print(coin_flips.count(True))

# 4.4
fav_artists.remove("Joji")
print(fav_artists)

# 4.5
cities["Toronto"] = 2930001
print(cities["Toronto"])

###############################
# Exercise 5

# 5.1
total_pop = 0
for pop in cities.values():
    total_pop += pop
print(total_pop)

# 5.2
for member, age in family_and_freinds.items():
    if age < 32:
        print(f"{member} is young")
    else:
        print(f"{member} is old")

# 5.3
print(fav_colors[-2:])

# 5.4
print(ages) # Printing original to make it easier to see if adding one to ages is implemented correctly
ages = list(map(lambda age: age + 1, ages))
print(ages)

# 5.5
fav_colors.append("Sea Green")
fav_colors.append("Coral Blue")
print(fav_colors)

###############################
# Exercise 6

# 6.1
movies = {1999 : ["The Matrix", "Star Wars Ep 1", "The Mummy"], 2009 : ["Avatar", "Star Trek", "District 9"], 2019: ["How to Train Your Dragon 3", "Tory Story 4", "Star Wars Episode 9"]}

# 6.2
phone_buttons = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]

# 6.3
countries = [{"Canada" : {"Continent" : "North America", "Island" : False}}, {"America" : {"Continent" : "North America", "Island" : False}}, {"Japan" : {"Continent" : "Asia", "Island" : True}}]

################################
# Exercise 7

# 7.1
for i in range(20):
    print("I will not skateboard in the halls")

# 7.1
skateboard_message = []
for i in range(20):
    skateboard_message.append("I will not skateboard in the halls")
print(len(skateboard_message)) # Shows length of the list. It should show 20

# 7.2
fifty_list = []
for i in range(50):
    fifty_list.append(i+1)
print(fifty_list) # Checking to see if it was added correctly

# 7.3
total = 0
for num in fifty_list:
    total += num
print(total)

# 7.4
triple_fifty = []
for i in range(50):
    for x in range(0, 3):
        triple_fifty.append(i+1)
print(triple_fifty)

# 7.5
not_island = []
for country in countries:
    for characteristics in country.values():
        if characteristics["Island"] == True:
            not_island.append(country)
print(countries)
print(not_island)

###################################
# Exercise 8

def sum_expenses(yearly_expense):
    total_expense = 0
    for expense in yearly_expense:
        total_expense += expense
    return total_expense

year1 = [92, 25, 83, 15, 67]
year2 = [100, 29, 58, 47, 12, 39, 28]

print(sum_expenses(year1))
print(sum_expenses(year2))

####################################
# Exercise 9

# 9.1
grocery_list = ["carrots", "toilet paper", "apples", "salmon"]
for grocery in grocery_list:
    print(f"* {grocery}")

# 9.1 continued
def print_groceries(list_of_groceries):
    for grocery in list_of_groceries:
        print(f"* {grocery}")
    return 0

grocery_list.append("rice")
print_groceries(grocery_list)

#9.2
print(len(grocery_list))

#9.3
if grocery_list.count("bananas") > 0:
    print("You don't need to pick up bananas today")
else:
    print("You need to pick up bananas")

# 9.4
print(grocery_list[1])

#9.5
sorted_grocery_list = sorted(grocery_list)
for grocery in sorted_grocery_list:
    print(f"* {grocery}")

#9.6
sorted_grocery_list.remove("salmon")
print(sorted_grocery_list)


###################################
# Exercise 10

# 10.1
students = {
  'cohort1': 34,
  'cohort2': 42,
  'cohort3': 22
}

# 10.2
def print_cohorts(cohort_dict):
    for cohort, num_students in cohort_dict.items():
        print(f"{cohort}: {num_students} students")
    print("")
    return 0

print_cohorts(students)

# 10.3
students["cohort4"] = 43
print_cohorts(students) # Checking tos ee it is added correctly
print("") # makes reading it in terminal easier

# 10.4
print(students.keys())

# 10.5
students = {cohort: num * 1.05 for cohort, num in students.items()}
print_cohorts(students)

# 10.6
del students["cohort2"]
print_cohorts(students)

# 10.7
total_students = 0
for num in students.values():
    total_students += num
print(total_students)

###################################
# Exercise 11
print("") # Making it easier to seperate the exercises in terminal

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("bitmaker")
    elif i % 3 == 0:
        print("bit")
    elif i % 5 == 0:
        print("maker")
    else:
        print(i)


###################################
# Exercise 12
print("") # Making it easier to seperate the exercises in terminal

def make_pizzas():
    counter = 0
    print("How many pizzas do you want to order?")
    quantity = int(input())
    while counter < quantity:
        print(f"How many toppings for pizza {counter + 1}")
        toppings = int(input())
        print(f"You have ordered a pizza with {toppings} toppings.")
        counter += 1
    return 0
make_pizzas()