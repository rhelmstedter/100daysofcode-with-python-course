import enchant
from itertools import permutations, combinations
from pprint import pprint as pp


name = 'extreme'
d = enchant.Dict("en_US")

perms_tuples = list(permutations(name, len(name)))
perms = [''.join(perm_tuple) for perm_tuple in perms_tuples]

combinations_tuples = list(combinations(name, len(name)//2 ))
combs = [''.join(combinations_tuple) for combinations_tuple in combinations_tuples]


print(len(set(perms)))
pp(set(perms))

print(len(combs))
pp(combs)
