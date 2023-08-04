import random
file = open('Game.txt', 'w+')
for i in range(0,10):
    j = random.randint(1,5)
    for x in range(0,j):
        file.write(str(i))
file.write('TREASURE')
for i in range(9,-1,-1):
    j = random.randint(1,5)
    for x in range(0,j):
        file.write(str(i))
file.close()
file = open('Game.txt','r')
move = input('Where you want to move? [1- forward 2-backwards]')
location = file.read()
len = len(location)
print(len)

stepss = 1
turns = 0

while True:
    if move == '1':
        steps = int(input('How many characters?'))
        if steps > len:
            print('try a lower number')
            steps = int(input('How many characters?'))
        stepss += steps

        new_location = location[stepss - 1]
        print(f"You Hit {new_location}")
        turns = turns + 1
        if new_location == 'T' or new_location == 'R' or new_location == 'E' or new_location == 'A' or  new_location == 'S' or new_location == 'U':
            print('You Won!!!')
            break
        else:
            move = input('Where you want to move? [1- forward 2-backwards]')
    elif move == '2':
        steps = int(input('How many characters?'))
        if steps > len:
            print('try a lower number')
            steps = int(input('How many characters?'))
            stepss += steps

        new_location = location[stepss - 1]
        turns = turns + 1
        print(f"You Hit {new_location}")
        if new_location == 'T' or new_location == 'R' or new_location == 'E' or new_location == 'A' or  new_location == 'S' or new_location == 'U':
            print('You Won!!!')
            break
        else:
            move = input('Where you want to move? [1- forward 2-backwards]')

print(f'you won in {turns} turns')