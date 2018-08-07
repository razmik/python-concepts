"""
Source: https://towardsdatascience.com/python-for-data-science-8-concepts-you-may-have-forgotten-i-did-825966908393
"""

x = [1,2,3,4]
out = []
for item in x:
    out.append(item**2)
print(out)

x = [1,2,3,4]
out = [item**2 for item in x]
print(out)