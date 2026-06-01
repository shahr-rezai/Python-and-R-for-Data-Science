#[ expression for item in iterable ]

squares = [x*x for x in range(5)]
print(squares)

marks = [80, 75, 90, 85, 70]
average = sum(marks)/len(marks)
print("Average =", average)
print("Highest =", max(marks))
print("Lowest =", min(marks))

