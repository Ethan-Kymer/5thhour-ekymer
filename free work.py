#Name:ethan kymer
#Class: 5th Hour
import random
roll=20





threevar= [random.randint(1,3),random.randint(1,3),random.randint(1,3)]

if threevar[0] == 1:
    roll*=.75
    print("cherry")
if threevar[1] == 1:
    roll*=.75
    print("cherry")
if threevar[2] == 1:
    roll*=.75
    print("cherry")
if threevar[0] == 2:
        roll *= 1.75
        print("diamond")
if threevar[1] == 2:
        roll *= 1.75
        print("diamond")
if threevar[2] == 2:
        roll*=1.75
        print("diamond")
if threevar[0] == 3:
         print("Goat")
if threevar[1] == 3:
         print("Goat")
if threevar[2] == 3:
         print("Goat")


if threevar[0] == 3 and threevar[1] == 3 and threevar[2] == 3:
    print("you win a Goat")
elif threevar[0] == 2 and threevar[1] == 2 and threevar[2] == 2:
    roll+=6000000
    print("you won the jack pot $6 $Million $dollars")
elif threevar[0] == 1 and threevar[1] == 1 and threevar[2] == 1:
    roll+=271000
    print("you win $271k")
else:
    print ("keep going, you got it next time")



wallet=roll+0
print(wallet)