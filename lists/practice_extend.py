list1 = input("Enter first list: ").split()
list2 = input("Enter second list: ").split()

list1.extend(list2)
print("Merged list:", list1)

list3 = list(map(int, input().split()))
list4 = list(map(int, input().split()))

list3.extend(list4)
print(list3)