#list1.extend(list2)
list1 = [1, 2, 3]
list2 = [4, 5]
list1.extend(list2)
print(list1)

letters = ['A', 'B']
letters.extend("CD")
print(letters)

words1 = ['kabul', 'Badakhshan']
words2 = ['kandahar']
words1.extend(words2)
print(words1)

#using extend with tuple

numbers = [1, 2]
numbers.extend((3, 4, 5))
print(numbers)

#using extend with sets
numbers1 = [1, 2]
numbers1.extend({3, 4})
print(numbers1)

#output order may change since set is not ordered but list is ordered
numbers2 = [1, 2]
numbers2.extend({4, 3})
print(numbers2)

classA = [80, 75, 90]
classB = [85, 70, 95]

classA.extend(classB)
print(classA)