n = int(input())

if n%2 == 0:
    print(n, 'is even')
else:
    print(n, 'is odd')

###########################

n = int(input())
print(f'{n} is {'even' if n%2 == 0 else 'odd'}')