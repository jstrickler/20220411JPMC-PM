file_path = "DATA/wombats.txt"
try:
    with open(file_path) as file_in:
        pass
except FileNotFoundError as err:
    # log error  (use python 'logging' module)
    # provide alternate value
    # exit program gracefully
    # ignore
    print(err)

colors = ['red', 'purple', 'orange', 'yellow', 'pink']
try:
    print(colors[9])
except IndexError as err:
    print(err)


nums = [0, 800, 80, 1000, 32, 4, 0, 255, 400, 5, 5000]
for num in nums:
    try:
        result = 10000 / num
    except ZeroDivisionError as err:
        print(err)
    else:
        print(result)




print("ALL DONE")