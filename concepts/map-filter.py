
"""
Specifically, map takes in a list and transforms it into a new list by performing some sort of operation on each element.
In this example, it goes through each element and maps the result of itself times 2 to a new list.
Note that the list function simply converts the output to list type.

source: https://www.youtube.com/watch?v=cKlnR-CB3tk
"""

# Map
seq = [1, 2, 3, 4, 5]
result = list(map(lambda var: var*2, seq))
print(result)

# Filter
seq = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x > 2, seq))
print(result)