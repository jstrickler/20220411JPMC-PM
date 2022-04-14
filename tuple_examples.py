
person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

x = [1, 2, 3]  # list
x = 1, 2, 3  # tuple
x = {1, 2, 3}  # set
x = (1, 2, 3)  # also a tuple
x = {'a': 1, 'b': 2, 'c': 3}  # dict

print(type(person), len(person))
print("person: {}".format(person))
print("person[0]: {}".format(person[0]))
print(person[0], person[1])

# it[0]  it[1] ...
#  var1, var2, ... = iterable
first_name, last_name, *_ = person
print(first_name, last_name)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

print("people[0]: {}".format(people[0]))
print("people[0][0]: {}".format(people[0][0]))
print("people[0][0][0]: {}".format(people[0][0][0]))

for first_name, last_name, product, dob in people:
    # first_name, last_name, produt, dob = people[0]
    # first_name, last_name, produt, dob = people[1]
    # ...
    print(first_name, last_name)
print('-' * 60)

state_capitals = [
    ('NC', 'Raleigh'),
    ('TX', 'Austin'),
    ('VA', 'Richmond'),
]
for state, capital in state_capitals:
    print(state, capital)
print()

values = 'a', 'b', 'c', 'd', 'e', 'f'
_, *fields, _, _ = values
print("fields: {}".format(fields))

flags = [True] * 10
print("flags: {}".format(flags))
data = [0] * 25
print("data: {}".format(data))
print('-' * 60)
print('>' +  ' ' * 10 + '<')

a = "abc"
b = "def"
c = a + b

x = [1, 2, 3]
y = [4, 5, 6]
z = x + y
print(c, z)

z +=  [7, 8, 9]
print(z)













