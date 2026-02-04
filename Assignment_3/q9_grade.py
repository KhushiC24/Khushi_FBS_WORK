eng = int(input('Enter English Marks: '))
maths = int(input('Enter Maths Marks: '))
marathi = int(input('Enter Marathi Marks: '))
hindi = int(input('Enter Hindi Marks: '))
ssc = int(input('Enter SSC Marks: '))

Total =  eng + maths + marathi + hindi + ssc
perc = (Total/500)*100
if  perc > 60:
    print('First Class')
elif perc > 50 and perc < 60:
    print('Second Class')
elif perc > 35 and perc < 50:
    print('Pass Class')
else:
    print('Failed')