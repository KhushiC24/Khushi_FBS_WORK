angle_1 = int(input('Enter 1st angle : '))
angle_2 = int(input('Enter 2nd angle: '))
angle_3 = int(input('Enter 3rd angle: '))

sum = angle_1 + angle_2 + angle_3

if angle_1 > 0 and angle_2 > 0 and angle_3 > 0 and sum == 180:
    print('Triangle is valid')
else:
    print('Triangle is not valid')