from text import normalize, tokenize, count_freq, top_n
import sys


def script():
    text = sys.stdin.read()
    # Получаем список всех слов
    text_corrected = tokenize(normalize(text))
    # Считаем общее кол-во слов
    count_words = len(text_corrected)
    # Получаем словарь уникальных слов
    dict_words = count_freq(text_corrected)
    # Считаем кол-во уникальных слов
    count_words_unique = len(dict_words)
    # Сортируем словарь по кол-ву слов
    dict_words_sort = top_n(dict_words)


    print(f'Всего слов: {count_words}')
    print(f'Уникальных слов: {count_words_unique}')
    print('Топ 5:')
    k = 0
    for word, counts in dict_words_sort.items():
        if k == 5:
            break
        k += 1
        print(f'{word}: {counts}')

