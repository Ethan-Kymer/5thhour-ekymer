#Name:
#Class: 5th Hour
#Assignment: HW16

import random
import math
#1. import the "random" library

#2. print "Hello World!"
print("hello")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
#4. Add a and b together, then divide the sum by c. Print the result.
ab = a + b
ac = ab/c
print(ac)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
print(round(ac))
if ac%2:
    print("this is even")
else:
    print("this is odd")
#6. Create a list of five different random integers between 1 and 10.
randint = [random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)]
#7. Print the 4th number in the list.
print(randint[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
randint.append(random.randint(1,10))
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
randint.sort(reverse=True)
print(randint[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i = 1
while i <= 100:
    print(i)
    i +=1
#11. Create a list containing the names of five other students in the classroom.
namelist = ["Ethan", "ethan", "gavin", "Helber", "Cruz"]
#12. Create a for loop that individually prints out the names of each student in the list.
for a in namelist:
    print(a)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
b=1
for b in range(1,100):
    print(b)
    b+=1
    if b%10 == 0:
        break


#14. Free space. Do something creative. :)

#i would  but class is about to end and i dont wanna submit it late XD