# program to combine two directories.

a = {1: 'aj', 2: 'bj', 3: 'cj'}
b = {4: 'aj', 5: 'bj', 6: 'cj'}

# using AND operation
print(a | b)

# using kwargs
print({**a, **b})

# using copy and update functions
c = a.copy()
c.update(b)
print(c)
