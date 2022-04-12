s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"
print(len(s1), len(s2), len(s5))
print(s1 == s2 == s3 == s4)
print("Guido's the ex-BDFL of Python")
print('Guido is the ex-"BDFL" of Python')
print("""Guido's the ex-"BDFL" of Python""")

query = """
select *
from customer_account
where customer_id == '1234'
"""

