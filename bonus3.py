import random

x = int(input('enter number:'))

for i in range(1, x + 1, 2):
    for _ in range(1, i + 1):
        print(_, end=" ")
    print()
for i in range(x - 2, 0, -2):
    for _ in range(1, i + 1):
        print(_, end=" ")
    print()



width= x * 2 - 1
for i in range(1,x+1):
    for _ in range(1, i + 1):
        print('  '*(x-i), end=" ")
    print('  '*(i*2-1))
for i in range(x - 1, 0, -1):
    print('  '*(x-i), end=" ")
    print('  '*(i*2-1))