a = "foo"
b = "bar"
print(a + b, '\n')

actor = "Chris Hemsworth"
print(actor, type(actor), len(actor), '\n')

print(actor.upper())
a1 = actor.upper()
print(actor.lower())
print(actor.count('h'), actor.count('H'))
print(actor.count('is'))
print(actor.lower().count('h'))
print(actor.startswith('Chris'), actor.startswith('Liam'))
print("is" in actor, "was" in actor)
print(actor.replace(' ', ''))
print(actor.replace('h', 'o'))
print(actor.replace('Chris', 'Liam'))
print(actor.isalpha())
print(actor.replace(' ', '').isalpha())
print(actor.find('Chris'), actor.find('Liam'))
print(actor.find('swo'), actor.find('ows'))
data = "red blue purple orange"
values = data.split()
print(values)
record = 'foo:bar:blah:baz'
print(record.split(':'))
print('/'.join(values))

s = "     All my exes live in Texas      "
print('|' + s + '|')
print('|' + s.lstrip() + '|')
print('|' + s.rstrip() + '|')
print('|' + s.strip() + '|')
print()

s = "xyxxyyxxxyyyxxxxyyyyAll my exes live in Texasxyxyxyxyxyxyxyx"
print('|' + s + '|')
print('|' + s.lstrip('xy') + '|')
print('|' + s.rstrip('xy') + '|')
print('|' + s.strip('xy') + '|')
print()

s = "$1000.28"
s = s.lstrip('$')
print(type(s))
print("s: {}".format(s))







