food = ['spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'spam']
ufood = set(food)
print("ufood: {}\n".format(ufood))

set1 = set()
for color in "red blue green orange yellow pink brown mauve".split():
    set1.add(color)

set2 = set('red red red orange green black white blue blue blue chartreuse'.split())
set2.add('purple')

print("set1: {}\n".format(set1))
print("set2: {}\n".format(set2))

print("COMMON:", set1 & set2)  # intersection
print("NOT COMMON:", set1 ^ set2)  # xor
print("BOTH:", set1 | set2)  # union
print("JUST set1:", set1 - set2)
print("JUST set2:", set2 - set1)
print()

for color in 'red', 'pink', 'magenta', 'orange', 'purple', 'brown':
    print(color, color in set1, color in set2)
print()

# [x, x, x, x, x, ...]   # list  store items for iteration
# {k:v, k:v, k:v, ...}   dict   look up something by a key
# {x, x, x, x, ...}   set   check for membership, remove dupes, compare sets for commonality or lack thereof
#  x, x, x   tuple   keep values together (i.e., record or struct)


