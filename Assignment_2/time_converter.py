hr = int(input('Enter time in Hour'))
min = int(input('Enter time in Minutes'))
sec = int(input('Enter time in Seconds'))

time = (hr * 3600) + (min * 60) + sec

print(f'Time converted into Seconds is {time}')