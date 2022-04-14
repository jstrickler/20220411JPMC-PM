d1 = dict()  # empty dict
print(d1, type(d1), len(d1))
d2 = {'a': 5, 'm': 8, 'b': 45}
print(d2, len(d2))
d3 = {}  # empty dict

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}
print(airports['RDU'])
print(airports["IAD"])
airports['ATL'] = "Atlanta"
airports['SEA'] = "Seattle/Tacoma"
print("airports: {}".format(airports))
print(airports.get('LAX'))
print(airports.get('LAX', "NOWHERE"))
del airports['OAK']
print("airports: {}".format(airports))

for code in 'LGA', 'JFK', 'EWR', 'BOS', 'IAD', 'BWI', 'YOW':
    print(code, code in airports)
print()

airports['CMH'] = "Columbus"
print("airports: {}".format(airports))
print(airports['YOW'])
del airports['MCO']

for code in 'LGA', 'JFK', 'EWR', 'BOS', 'IAD', 'BWI', 'YOW':
    print(code, airports.get(code, 'NOT FOUND'))
print()

for code, city in airports.items():
    print(code, city)
print()
print(airports.items())
print(airports.keys())
print(airports.values())

