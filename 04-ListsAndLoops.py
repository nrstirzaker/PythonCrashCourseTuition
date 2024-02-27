# shoppingList = ['Potatoes', 'Pasta', 'Cheese', 'Mushrooms',"Butter", "Bread","Milk"]

# print(shoppingList)

# for item in shoppingList:
#    print(item)
# print("The end")    

# for thing in shoppingList:
#    print(thing)


# print(shoppingList[2:5])

# print("---Break---")
# shoppingList = ['Potatoes', 'Pasta', 'Cheese', 'Mushrooms',"Butter", "Bread","Milk"]
# for item in shoppingList:
# if item == "Mushrooms":
#    break
#
#   print(item)    


# print("---Continue---")
# shoppingList = ['Potatoes', 'Pasta', 'Cheese', 'Mushrooms',"Butter", "Bread","Milk"]
# for item in shoppingList:
#  if item == "Mushrooms":
#    continue
#  print(item)   

stream = [1.0, 2, 3.00, 4, 3.5, 7.2, 0.1, -8, -2.9, "END"]
intList = []
fltList = []

for num in stream:
    if type(num) is int:
        intList.append(num)
    elif type(num) is float:
        fltList.append(num)

print(intList)
print(fltList)
