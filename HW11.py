#Name:Ethan kymer
#Class: 5th Hour
#Assignment: HW11

import random
#1. Print "Hello World!"
print("do you actually read these?")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
thdlist=[random.randint(1,100),random.randint(1,100),random.randint(1,100)]
#3. Print the list.
print(thdlist)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.

if thdlist[0]>thdlist[1] and thdlist[0]>thdlist[2]:
    print("this is the highest number:",thdlist[0])
    num = thdlist[0]

elif thdlist[1]>thdlist[0] and thdlist[1]>thdlist[2]:
    print("this is the highest number:",thdlist[1])
    num = thdlist[1]

else:
    print("this is the highest number:",thdlist[2])
    num = thdlist[2]
#5. Tie the result (the largest number) from #4 to a variable called "num".
print(num)
#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.

if num%2:
        print("this is divisable by 2:")
elif num%3:
        print("this is divisable by 3:")
else:
        print("this is divisable by nothing:")