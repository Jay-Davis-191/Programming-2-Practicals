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

for x in count_list:
    print("{:10}: {:5}".format(x, count_list[x]))
