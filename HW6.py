#Name:
#Class: 5th Hour
#Assignment: HW6


#1. Create a list with 9 different numbers inside.
list=[0,1,2,3,4,5,6,7,8]
#2. Sort the list from highest to lowest.
list.sort(reverse=True)
#3. Create an empty list.
mtlist=[]
#4. Remove the median number from the first list and add it to the second list.
list.remove(4)
mtlist.append(4)
#5. Remove the first number from the first list and add it to the second list.
list.remove(0)
mtlist.append(0)
#6. Print both lists.
print(list)
print(mtlist)
#7. Add the two numbers in the second list together and print the result.
adlist= mtlist[0] + mtlist[1]
print(adlist)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
list.append(4)
#9. Sort the first list from lowest to highest and print it.
list.sort(reverse=False)
print(list)