N = int(input('N = '))
k = int(input('k = '))
i = 2
for count in range(k):
    while i ** count < N:
        print(i ** count)
        count += 1