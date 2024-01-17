import random
counts = 3
answer = random.randint(1,11)
while counts > 0:
    temp = input("what number I am thinking of? ")
    guess = int(temp)

    if guess == answer:
        print("right")
        print("but no prize")
        break

    else:
        if guess < answer:
            print("wrong")
            print("too small, try again")
        
        else: 
            print("wrong")
            print("too large, try again")
            counts = counts - 1

print("game over")
