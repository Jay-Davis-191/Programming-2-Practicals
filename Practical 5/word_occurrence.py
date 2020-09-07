def word_count(str):
    counts = dict()
    words = str.split()
    words = sorted(words)
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


print("Please enter a sentence")
inputted_string = (input(">>> ")).lower()
count_list = word_count(inputted_string)
longest_word = max(count_list, key=len)

for x in count_list:
    print("{:{}} = {}".format(x, len(longest_word), count_list[x]))
