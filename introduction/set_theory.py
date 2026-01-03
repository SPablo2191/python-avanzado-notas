set_one = {1, 2, 3, 4, 5}
set_two = {4, 5, 6, 7, 8}

# UNION
union_set = set_one | set_two
print("Union:", union_set)

# INTERSECTION
intersection_set = set_one & set_two
print("Intersection:", intersection_set)

# DIFFERENCE
difference_set = set_one - set_two
print("Difference (set_one - set_two):", difference_set)

difference_set = set_two - set_one
print("Difference (set_two - set_one):", difference_set)

# SYMMETRIC DIFFERENCE
symmetric_difference_set = set_one ^ set_two
print("Symmetric Difference:", symmetric_difference_set)