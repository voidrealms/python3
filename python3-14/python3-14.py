#Simple app - paint calculator

#How much paint is needed

print('Paint calculator')
print('Enter a wall size as width, height in feet or press enter to stop')
print('Example: 12,8')

#Variables
walls = [] #List of walls measurements
gallons  = 1 / 350 #One gallon covers 350 sqft
total = 0 #Total gallons to buy

#Get the user input
while True:
    s = input('Enter a wall size:')
    if len(s) == 0: break

    #Verify the input
    sqft = s.split(',')
    if len(sqft) < 2:
        print('Invalid format')
        break

    #Convert the strings to ints
    w = int(sqft[0])
    h = int(sqft[1])
    item = [w,h]
    walls.append(item)
    print(f'Adding wall: {item}')

#Calculate the numbers
print(f'You entered {walls}')
for m in walls:
    w = m[0]
    h = m[1]
    s = w * h
    v = s * gallons
    total += v
    
print(f'You need to buy {round(total,2)} gallons of paint')






