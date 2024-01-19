#Alexander Blad
from math import pi
from datetime import datetime

current_date_time=datetime.now()
w=int(input('Please input the width of the tire in mm: '))
a=int(input('Please input the aspect ratio of the tire: '))
d=int(input('Please enter the diameter of the wheel in inches: '))


v = pi*w**2*a*(w*a +(2540*d))/10000000000 #volume calculation
#Make sure to have ALL mathematical operators so that
#You don't call one the floats 

print(f'The approximate volume of this tire is {v:.2f} liters.')

purchase=input('Would you like to buy these tires?: Y/N ')

if purchase=='Y' or purchase=='y':
    phone_number=input('Please enter your phone number: ')

with open('volumes.txt', 'at') as volumes_file:
    if purchase=='Y' or purchase=='y':
        print(f'{current_date_time:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}', file=volumes_file)
        print(phone_number, file=volumes_file)
    else:
        print(f'{current_date_time:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}', file=volumes_file)