#hard coded values
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#creating an empty list to store the non-repeated elements
temp_list = []

for i in range(0, len(my_list)):
    #if the value isn't in the list, it indicates a new value and appends it to the temp list
    if my_list[i] not in temp_list:
        temp_list.append(my_list[i])
     #if the value is already in the temp list, it would skip and execute to the next element in the list   
    if my_list[i] in temp_list:
        continue

#merging the contents from temp list to the original list
my_list = temp_list[:]

print("The list with unique elements only:")
print(my_list)
