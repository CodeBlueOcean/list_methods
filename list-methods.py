# basket = [1,2,3,4,5]

# #adding
# new_list = basket.append(100)
# print(basket)
# print(new_list)



## or another example

# basket = [1,2,3,4,5]

# #adding
# basket.append(100)
# new_list = basket
# print(basket)
# print(new_list)

## or another example

basket = [1,2,3,4,5]

#adding
basket.insert(4, 100)
new_list = basket
print(basket)
print(new_list)

## or another example

basket = [1,2,3,4,5]

#adding
new_list = basket.insert(4, 100)
print(basket)
print(new_list)

## or another example

basket = [1,2,3,4,5]

#adding
new_list = basket.extend([100, 101])
print(basket)
print(new_list)

## or another example

basket = [1,2,3,4,5]

#adding
new_list = basket.extend([100, 101])
print(basket)
print(new_list)

#removing
basket.pop()
basket.pop(0)
print(basket)

#removing
new_list = basket.remove(4)
print(basket)

#removing
# new_list = basket.pop(4)
# print(basket)

#removing
new_list = basket.clear()
print(basket)
