mylist1 = [10, 20, 30, 40,50]
mylist2 = ["apple", "banana", "cherry"]
mylist3 = [10, "apple", 20, "banana"]
mylist = list()     #empty list

# print(mylist1)
# print(mylist2)
# print(mylist3)
# print(mylist)

#Example 2 #Accessing items from the list
#-------------------

# mylist5 = ["apple", "banana", "cherry"]   #indexing starts from 0
#
# print(mylist5[1])    #banana
# print(mylist5[-3])   #apple


#example 3: Range of indexes
#------------------------------
# mylist5 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(mylist5[2:5])   #['cherry', 'orange', 'kiwi']
#
# print(mylist5[-4:-1])    # ["orange", "kiwi", "melon"]

#Example 6 ---append()
mylist5 = ["apple", "banana", "cherry"]
mylist5.append("orange")
print(mylist5)