import collections

def delete_repeating_phrases(filename):
    # read the file and split it into words
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        for sym in '.,:;«»“”!?—"()':
            text = text.replace(sym, '')
        text = text.lower()
    words = text.split()

    # create a list of phrases of length 3 or more
    phrases = []
    for i in range(len(words) - 2):
        phrase = ' '.join(words[i:i+3])
        if len(phrase.split()) >= 3:
            phrases.append(phrase)
    counter = collections.Counter(phrases)
    print(counter)

delete_repeating_phrases('file.txt')