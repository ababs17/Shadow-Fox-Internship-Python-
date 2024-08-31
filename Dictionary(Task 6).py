# list of riends
friends = ["Fred", "Jerry", "Finlye", "Abene","Mustapha","Sheldon"]
friends=[('Fred', 5), ('Jerry', 5), ('Finlye', 6), ('Abena', 5), ('Mustapha', 8),('Sheldon',7)]


#Partner and I
my_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

#  the total expenses for us
mytotal = sum(my_expenses.values())
partnertotal = sum(partner.values())

# output of total expenses for us
print("my total expenses: $", mytotal)
print("Partner's total expenses: $", partnertotal)

# who spent more money
if mytotal > partnertotal:
    print("I spent more money than she did.")
elif partnertotal >mytotal:
    print("She spent more money than I.")
else:
    print("We spent the same amount of money.")

# who spent the most
max_diff_category = None
max_diff = 0
for category in my_expenses:
    diff = abs(my_expenses[category] - partner[category])
    if diff > max_diff:
        max_diff = diff
        max_diff_category = category

# category and the difference spending
print("The category is:", max_diff_category)
print("The difference is: $", max_diff)
