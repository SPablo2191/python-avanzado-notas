new_set = set()
# ADD
new_set.add(1)
print(new_set)
new_set.add(1)
new_set.add(1)
new_set.add(1)
print(new_set)

# REMOVE
# new_set.remove(1)
# print(new_set)
# new_set.remove(1)
# print(new_set)

# DISCARD
new_set.discard(2)  # No error even if 2 is not in the set
print(new_set)

# POP
popped_element = new_set.pop()
print("Popped element:", popped_element)

# CLEAR
new_set.clear()
print("Set after clear:", new_set)