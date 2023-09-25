coins = int(input('n = '))
eagle = 1
tails = 0
coup = 0    # 0 -> 1
recoup = 0  # 1 -> 0
for n in range(coins):
    version = int(input('x (1 or 0) = '))
    if version == tails:
        coup += 1
    elif version == eagle:
        recoup += 1
    else:
        print ("Pleas enter the coorect value")
if coup > recoup:
    print (f"to need {recoup}")
else:
    print (f"to need {coup}")