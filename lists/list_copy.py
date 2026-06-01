#A shallow copy copies only the outer list, not the inner objects.
import copy

original = [[1, 2], [3, 4]]
#shallow = copy.copy(original)

#shallow[0][0] = 99

print(original)
#print(shallow)

#A deep copy copies everything, including nested objects.
deep = copy.deepcopy(original)
deep[0][0] = 99;
print(original)
print(deep)