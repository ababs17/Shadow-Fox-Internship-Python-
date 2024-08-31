def format_number(number, format_spec):
    return format(number, format_spec)


result = format_number(145, 'o')
print(f"Answer: {result}")

print("\nReason:")
print("The 'o' format specifier is used for octal representation.")
print(f"145 in decimal is equivalent to {result} in octal.")

import math


PI = 3.14
RADIUS = 84  
WATER_PER_SQ_METER = 1.4  

# Calculate pond area
pond_area = PI * (RADIUS ** 2)
print(f"Case 1: Area of the pond")
print(f"Area = π * r^2 = {PI} * {RADIUS}^2 = {pond_area:.2f} sqm")

water_volume = pond_area * WATER_PER_SQ_METER
print(f"\nStep 2: Calculate the total amount of water in the pond")
print(f"Water volume = Pond area * Water per sqm")
print(f"Water volume = {pond_area:.2f} * {WATER_PER_SQ_METER} = {water_volume:.2f} liters")

# output result
print(f"\nFinal Result:")
print(f"The total amount of water in the pond is {int(water_volume)} liters.")

#  values
distance = 490  
minutes = 7  

# Convert t to s
seconds = minutes * 60


speed = distance // seconds  

# output the speed
print(speed)
