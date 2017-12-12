# Linear search using Python

numlist = [1,3,4,5,8,6,10,12]
num_search = int(input("Enter the number to search:"))

for i in range(len(numlist)):
    if numlist[i] == num_search:
        print("The number is present in the list at position", i)
        break
else:
    print("The number is not in the list")


