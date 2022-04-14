list1 = list()   # empty list
list2 = ['spam', 'ham', 'toast', 'eggs']
print(list2[0], list2[3])
list3 = []

cities = ['Dallas', 'Jersey City', 'Plano', 'Tampa', "Lakeland",
          'Durham', 'New York', 'San Francisco']

print("cities: {}".format(cities))
print(len(cities))

cities.insert(0, 'San Diego')
cities.insert(0, 'Portland')
print("cities: {}".format(cities))
cities.insert(4, "Seattle")
cities.insert(2, "Spokane")
print("cities: {}".format(cities))
cities.append('Cincinnati')
cities.append('Albany')
print("cities: {}".format(cities))
more_cities = ['Boston', 'Savannah', 'Richmond', 'Madison']
cities.extend(more_cities)
print("cities: {}".format(cities))

# LIST.insert(pos, obj)  LIST.append(obj)  LIST.extend(iterable)
# cities += more_cities
# print("cities: {}".format(cities))
del cities[2]
print("cities: {}".format(cities))

city = cities.pop()
print("city: {}".format(city))
print("cities: {}".format(cities))

city = cities.pop(3)
print("city: {}".format(city))
print("cities: {}".format(cities))

cities.remove('Lakeland')
print("cities: {}".format(cities))

#  del LIST[pos]  LIST.pop(pos=-1)    LIST.remove(value)

print(cities[0], cities[5], cities[-1], cities[-3])
print(cities[len(cities) - 1])
cities[0] = "Bend"
print("cities: {}".format(cities))

print("cities[0:4]: {}".format(cities[0:4]))
print("cities[:4]: {}".format(cities[:4]))
print("cities[5:8]: {}".format(cities[5:8]))

food = "Butter Chicken"
print(food[:6])
print(food[-7:])
print("cities: {}".format(cities))

print("cities[-2:-1]: {}".format(cities[-2:-1]))
print("cities[-2:] {}".format(cities[-2:]))


#  del x   len(x)  x.pop()

#  del(x)
#  del x
print('-' * 60)
for city in cities:
    if (len(city) > 5) and city.startswith('B'):
        print(city)
print()

s = "abc"
for char in s:
    print(char.upper())
print()

# iterables: str bytes list tuple set dict <generator>


colors = ['red', 'purple', 'blue', 'orange', 'mauve', 'ecru']
nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

print(len(colors), min(colors), max(colors), sorted(colors))
print(len(nums), min(nums), max(nums), sorted(nums), sum(nums))
print()

for i, color in enumerate(colors):
    print(i, color)
print()
print(list(enumerate(colors)))

e_colors = enumerate(colors)
# print(len(e_colors))
# print(e_colors[0])

for i, color in e_colors:
    print(i, color)

rcolors = reversed(colors)
print(rcolors)
for color in rcolors:
    print(color)
print()

r = range(10)
print(r)
for i in r:
    print("Wombat!")
print()

# range(stop)  range(start, stop) range(start, stop, step)

for i in range(1, 6):
    print(i, "robot")
print()

e = enumerate(colors)
wombat1 = e  # alias
wombat1 = e
list1 = list(e)  # consume
list2 = list(e)
print(list1)
print(list2)

e = enumerate(colors)
x, y, *z  = e  # unpack
print(x)
print(y)
print(z)
print(list(e))

