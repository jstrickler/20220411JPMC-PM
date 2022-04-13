i = 0
while i < 3:
    print(i, "Python!")
    i += 1
print('-' * 60)

while True:
    user_name = input("Enter user name: ")
    if user_name == 'q':
        break  # exit loop
    if user_name == '':
        continue  # go to top
    print(f"Adding {user_name}")


