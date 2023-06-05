import collections

def delete_repeating_phrases(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read() # чтение текстового файла
        for sym in '.,:;«»“”!?—"()':
            text = text.replace(sym, '') # все ненужные для анализа символы заменяются на пустые
        text = text.lower() # текст переводится в нижний регистр
    words = text.split() # текст делится на слова

    phrases = []
    for i in range(len(words) - 2):
        phrase = ' '.join(words[i:i+3]) # создаются все возможные фразы, состоящие из трёх поряд идущих слов
        if len(phrase.split()) >= 3:
            phrases.append(phrase) # эти фразы добавляются в список
    counter = collections.Counter(phrases) # происходит подсчёт совпадений фраз в списке
    print(counter)

delete_repeating_phrases('file.txt')
