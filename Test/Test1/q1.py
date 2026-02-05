length = float(input('Enter Length: '))
breadth =float(input('Enter Breadth: '))
radius = float(input('Eneter Radius: '))

Area_r = length * breadth
area__c = 3.14 * radius ** 2

area_s = (Area_r - length) + (area__c / 2)

perimeter_r = 2 * (length +breadth)
perimeter_c = 2 * 3.14 * radius 

perimeter_s = (perimeter_r - length )+ (perimeter_c/2)

print(f'Area {area_s} and periimeter {perimeter_s}')