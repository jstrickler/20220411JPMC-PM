
file_path = "DATA/mary.txt"

mary_in = open(file_path, "r")
# read file here ...
mary_in.close()

with open(file_path) as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print('-' * 60)

with open(file_path) as mary_in:
    contents = mary_in.read()
    print("RAW:")
    print(repr(contents))
    print("normal:")
    print(contents)
print('-' * 60)

with open(file_path) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

with open(file_path) as mary_in:
    all_lines_without_nl = [line.rstrip("\n\r") for line in mary_in]
    print(all_lines_without_nl)
print('-' * 60)

#  FILE.seek()  FILE.tell()

target = 'z'
output_file_path = f"{target}_files.txt"
with open('DATA/words.txt') as words_in:
    with open(output_file_path, "w") as words_out:
        for raw_word in words_in:
            if raw_word.startswith(target):
                words_out.write(raw_word)








