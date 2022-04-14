counts = {}

with open('DATA/words.txt') as words_in:
    for word in words_in:  # read each line
        ch = word[0]
        counts[ch] = counts.get(ch, 0) + 1
        # if ch in counts:
        #     counts[ch] = counts[ch] + 1
        #     #  counts[ch] += 1
        # else:
        #     counts[ch] = 1

for ch, count in counts.items():
    print(ch, count)
