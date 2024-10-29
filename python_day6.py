# ## creating an empty list

# empty_list = list()

# print("empty_list")

# ## creating another with 2, 3, 4

# list_nums = list([2, 3, 4])

# print(list_nums)

# ## alternative
# list_nums2 = list([5, 6, 7])

# print(list_nums2)

# user_name = "Paul"

# ## access the element within a list
# ## [] = index operator

# # print(list_nums2[0]) 
# # print(list_nums2[1])
# # print(list_nums2[2])

# # ## to easily get all elements in the list 
# # for each_item in list_nums:
# #     print(each_item)

# # for each_item in list_nums2:
# #     print(each_item)    

# ## accessing all igtems within a lis
# for seq in range(0, len(list_nums)):
#     print(len(list_nums))


# ## let return the size
#     print("------------------------")
#     print(list_nums)


# house_item = ["car", 3, "dog", 2, "tv", "boy"]  

# ## list slicing
# print("--------------------------------")
# print(house_item[0:1])
# print(house_item[0:3])
# print(house_item[2:6])

# print("-------------------------")
# ## adding a new element to the list
# house_item.append("girl")
# print(house_item)

# ## extending a list 
# house_item.extend(list_nums)
# print(house_item)

#  ## insert an item in  a new list
# house_item.insert(0, "pen")
# print(house_item)

# ## removing item from a list

# house_item.remove("dog")
# print(house_item)

# ## return the index of  an element within a list 
# print(house_item.index("girl"))

## creating an empty list 
# fav_sports = []

# ## ask user their fav sports 
# user_input = input("Enter your fav sports: ")

# ## adding user input to the original list
# fav_sports.append(user_input)

# ## ask user their fav sports team
# user_input = input("what team do you support in that sports: ")
# ## add that to the original list
# fav_sports.append(user_input)
# print(fav_sports)


## ways of creatind dic
# dict() , () key : value
my_dict = {
    "name": "John", "age": 30, "city": "New Yourk"
}

class_records = {
                1 : {"sam Tugga", "class 6"},
                2 : {"Lydia Menash", "class 6"},
                3 : {"Hassan Musah", "class 6"}
                }
# print(my_dict["age"])
# print(my_dict["city"])
# print(my_dict["name"])

print(class_records[1])

## return all the keys in a dictionary 
print(class_records.keys())

## return all the values in a dictionary
print(class_records.values())

## insert a new record in the dictionary
class_records[4] = {"Shadrack ", "class 6"}


print(class_records)
## class_records.clear()
print("-------------------------")
var = class_records.keys()
for each_item in var:
    print(class_records[each_item])