import operator
words_dictionary={}
def load_data(filepath):
    with open(filepath) as data_file:
        lines = data_file.read().splitlines()
        lines = list(line for line in lines if line!='')
    return lines


def get_most_frequent_words(text):
    words = text.split()
    for word in words:
        word = word.lower()
        
        if word!='-':
            if not (word[-1]).isalpha():
                word = word[:-2]
            else:
                if word not in words_dictionary:
                    words_dictionary[word] = 1
                else:
                    words_dictionary[word] += 1

if __name__ == '__main__':
    lines = load_data("howToBeProgrammer.txt")
    for line in lines:
        get_most_frequent_words(line)

    words_dictionary = sorted(words_dictionary.items(), key=lambda x: x[1], reverse = True)
    
    for i in range(10):
        print("%s => %s" % (words_dictionary[i][0], words_dictionary[i][1]))
