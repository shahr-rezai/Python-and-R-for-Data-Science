list1 = [1, 2, 3]
list1 += [4, 5]

print(list1)

#common mistakes 

numbers = [1, 2]

#numbers.extend(5)
#wrong because integer is not iterable

#numbers.extend([5])
#correct list is iterable
