feet = int(input('Enter Value in Feet'))

Inches = int(input('Enter Value in Inches '))

meter = (feet * 0.3048) + (Inches * 0.0254)

centimeter = (feet * 30.48) + (Inches * 2.54)

print(f'Distance given in Feet And Inches in Meter and Centimeter are {meter}m {centimeter}cm')