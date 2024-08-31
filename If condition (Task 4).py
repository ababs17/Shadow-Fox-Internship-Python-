'''def calculate_bmi(height, weight):
    return weight / (height ** 2)

def determine_category(bmi):
    if bmi >= 30:
        return "Obesity"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    else:
        return "Underweight"

# take input from user 
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))


bmi = calculate_bmi(height, weight)

category = determine_category(bmi)

# output result
print(f"Your BMI is {bmi:.2f}")
print(f"BMI Category: {category}")'''

#  lists of cities in country
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]


countries = {
    "Australia": Australia,
    "UAE": UAE,
    "India": India
}

def findcountry(city):
    for country, cities in countries.items():
        if city in cities:
            return country
    return None

# take  input from user
city = input("Enter a city name: ").strip()

country = findcountry(city)

#output result
if country:
    print(f"{city} is in {country}")
else:
    print(f"Sorry, {city} is not in our database.")