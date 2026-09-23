#Name:
#Class: 5th Hour
#Assignment: HW8


#1. Import the "random" library
import random
#2. print "Hello World!"
print("hello")
#3. Create three different variables that each randomly generate an integer between 1 and 10
ranint1=random.randint(1,10)
ranint2=random.randint(1,10)
ranint3=random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print(ranint1,ranint2,ranint3)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
ranintadd= ranint1 + 2
ranintsub = ranint1 - 4
ranintmul = ranint1 * 1.5
#6. Print each result from #5 on the same line.
print(ranintadd, ranintsub, ranintmul)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
randomlist=[random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
#8. Sort the list in #7 and print it.
randomsorted=sorted(randomlist)
print(randomsorted)
#9. Add together the highest three numbers in the list from #7 and print the result.
addrando=(randomlist[1]+randomlist[2]+randomlist[3])
print(addrando)
#10. Create a list with 5 names of other students in this class and print the list.
namelist=["Ethan","ethan","gavin","cruz","coach mack"]
print(namelist)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(namelist)
print(namelist)
#12. Print a random choice from the list of names from #10.
classnumchoice=random.choice(namelist)
print(classnumchoice)