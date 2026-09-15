#Name:Ethan kymer
#Class: 5th Hour
#Assignment: HW6


#1. Create a list with 9 different numbers inside.
list=[0,1,2,3,4,5,6,7,8]
#2. Sort the list from highest to lowest.
list.sort(reverse=True)
#3. Create an empty list.
mtlist=[]
#4. Remove the median number from the first list and add it to the second list.
poplist=list.pop(4)
mtlist.append(poplist)
#5. Remove the first number from the first list and add it to the second list.
pop2=list.pop(0)
mtlist.append(pop2)
#6. Print both lists.
print(list)
print(mtlist)
#7. Add the two numbers in the second list together and print the result.
adlist= mtlist[0] + mtlist[1]
print(adlist)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
list.append(adlist)
#9. Sort the first list from lowest to highest and print it.
list.sort()
print(list)