#Creating a tuple
numbers = (1,2,3,4,5,6)
print(numbers)
print(type(numbers))

#Accessing items in a tuple
numbers = (1,2,3,4,5,6)
print(numbers[1])
print(numbers[3])
print(numbers[-2])
print(numbers[:3])

#Adding Items in a Tuple
numbers = (1,2,3,4,5,6)
numbers_add = numbers+(7,8,9)
print(numbers_add)

#Removing Items From A Tuple
numbers = (1,2,3,4,5,6)
num1 = list(numbers)
print(num1)
num1.remove(5)
print(num1)

#Converting the list back to a tuple
num1 = tuple(num1)
print(num1)
print(type(num1))