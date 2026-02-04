
age_1 = int(input('Enter Age_1: '))
ticket_1 = int(input("Enter Ticket 1st amount"))
age_2 = int(input('Enter Age_2: '))
ticket_2 = int(input("Enter Ticket 2nd amount"))
age_3 = int(input('Enter Age_3: '))
ticket_3 = int(input("Enter Ticket 3rd amount"))
age_4 = int(input('Enter Age_4: '))
ticket_4 = int(input("Enter Ticket 4th amount"))
age_5 = int(input('Enter Age_5: '))
ticket_5 = int(input("Enter Ticket 5th amount"))

# Person 1
if age_1 < 12:
    pay1 = ticket_1 * 0.70
elif age_1 > 59:
    pay1 = ticket_1 * 0.50
else:
    pay1 = ticket_1

# Person 2
if age_2 < 12:
    pay2 = ticket_2 * 0.70
elif age_2 > 59:
    pay2 = ticket_2 * 0.50
else:
    pay2 = ticket_2

# Person 3
if age_3 < 12:
    pay3 = ticket_3 * 0.70
elif age_3 > 59:
    pay3 = ticket_3 * 0.50
else:
    pay3 = ticket_3

# Person 4
if age_4 < 12:
    pay4 = ticket_4 * 0.70
elif age_4 > 59:
    pay4 = ticket_4 * 0.50
else:
    pay4 = ticket_4

# Person 5
if age_5 < 12:
    pay5 = ticket_5 * 0.70
elif age_5 > 59:
    pay5 = ticket_5 * 0.50
else:
    pay5 = ticket_5

total = pay1 + pay2 + pay3 + pay4 + pay5

print("Total amount:", total)
