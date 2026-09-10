#Name:
#Class: 5th Hour
#Assignment: HW5

#1. Print Hello World!
print("hello")
#1. Create a list with 5 strings containing 5 different names in it.
thelist=["one", "two", "three", "four", "five"]
#2. Append a new name onto the Name List.
thelist.append ("six")
#3. Print out the 4th name on the list.
print(thelist[3])
#4. Create a list with 4 different integers in it.
numlist=[1,2,3,4,5]
#5. Insert a new integer into the 2nd spot and print the new list.
numlist.insert(1, 6)
print(numlist)
#6. Sort the list from lowest to highest and print the sorted list.
numlist.sort()
print(numlist)
#7. Add the 1st three numbers on the sorted list together and print the sum.
numsum=numlist[0]+ numlist[1] + numlist[2]
print(numsum)
#8. Create a list with two strings, two variables, and too boolean values.
mixed= ["left", "right", 5, 6, True, False]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(mixed[int(input("enter a index value:"))])
