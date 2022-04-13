person = "John Doe"
city = "New York"
value = 38.39203993032

print(person, city, value)
# output str(person) + ' ' + str(city) + ' ' + str(value) + '\n'
print("----")

print(person, city, value, sep="")
print(person, city, value, sep="/")
print(person, end=',')
print(city, end=':')
print(value)

s = f"{person} lives in {city}"
print(s)
s = "{} lives in {}".format(person, city)  # pre-3.6
print(s)
print(f"2 + 2 = {2 + 2}")

print(f"Value is {value}")
print(f"Value is {value:.2f}")
count = 32
print(f"Count is {count:5d}")
print(f"Count is {count:05d}")
n = 3236723097209
print(f"{n:,d}")










