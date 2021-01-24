all_words = []
def parse_words():
    f = open('word_rus.txt')
    for word in f:
        all_words.append(word[0:-1])

def get_words():
    return all_words