#Name:ethan kymer
#Class: 5th Hour
#Assignment: HW15
from asyncio import events

#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.
i = 5
for i in range(5, 0,-1):
    print(i)
#2. Create a for loop that counts up and prints only even numbers between 1 and 30.
a = 31
for a in range(2,a,2):
    print(a)
#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.
b = 30
for b in range(1,b,1):
    if b%3==0:
        print(b)

#4. Create a for loop that prints 5 different animals from a list.
anlist=["orangutan","bear","fly","pigeon","coach mack when hes programming"]

for anlist in anlist:
    print(anlist)
#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
revspell=input("enter word:")
revrevspell=revspell[::-1]
print(revrevspell)
#6. Create a list containing 10 integers of your choice and print the list.
tenlist=[4,2,7,1,5,6,3,8,9,11]
#7. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers=0
oddNumbers=0
#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.
for z in tenlist:
    if z%2==0:
        evenNumbers+=1
    else:
        oddNumbers+=1
print(evenNumbers)
print(oddNumbers)


#9. Create a variable that asks the user for an integer and an empty integer variable.
inting=int(input("enter number:"))
integ1=0
#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)
for x in range(1,inting+1):
    integ1+=x
print(integ1)