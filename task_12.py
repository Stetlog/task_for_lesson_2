P = int(input('P = '))
S = int(input('S = '))
x = 0
y = 0
while x * y != P and x + y != S:
    x += 1
    y += 1
    if x == y:
        x -= 1

print (x,y)  #она так-то работает, но значение показывает ВСЕГДА