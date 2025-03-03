print("Inbuit Data types")

list_demo = ["Dipanjan","Ishita","Krishanu","Riya","Mallika"]

inde = list_demo.index("Krishanu")

print(inde)

print("Number of Dipanjan : ",list_demo.count("Dipanjan"))

list_demo.sort()

print(f"Sort version of List {list_demo}")

list_demo.reverse()

print("reverse version of List ",list_demo)

print("List comprehension")

list1 = [ num**2 for num in range(10) if num%2==0]

print(list1)

for index,value in enumerate(list_demo):
    print(index,value)


print(f"Sorted list {sorted(list1,reverse=True)}")

print(list1 * 3)

print(list1 + [1,2,3])

print("Tuples are immutable")
print("Packing and unpacking of tuple")

tup = "Dipanjan","Krishanu","Ishita"
print(type(tup))
name,*all = tup
print(name)
print(all)
all.clear()
print(all)

l1 = [2,3,4,5]
l2 = [3,4,5,6]

union_l = set(l1).union(set(l2))
print(union_l)

l1 = [2,3,4,5]
l2 = [3,4,5,6]
sd_set = set(l1).symmetric_difference(set(l2))
print(sd_set)

print("The set has two important functions issubset() and issuperset()")

dict1 = {"name" : "Dipanjan",
         "age" : 38,
         "address" : "Amsterdam"}
print(dict1)

shallow_copy = dict1.copy()
print(shallow_copy)

print("merging of two dictionaries")

d2 = {"name" : "Ishita",
      "age" : 38,
      "address" : "Pune"}
merge_dict = {**dict1,**d2}
print(f"Merged dictionary is {merge_dict}")

from collections import defaultdict

default_dict = defaultdict(list)
print(default_dict)
default_dict['a'].append(1)
default_dict['a'].append(2)
default_dict['b'].append(3)
print(default_dict)





