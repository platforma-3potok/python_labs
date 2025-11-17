from text import normalize, tokenize, count_freq, top_n

def script():
    text = input()
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
    print()
    print('Топ 5:')
    
    # Находим максимальную длину слова и частоты в топ-5
    max_word_len = max(len(word) for word, _ in dict_words_sort[:5])
    max_count_len = max(len(str(count)) for _, count in dict_words_sort[:5])
    
    # Устанавливаем ширину колонок (минимум 15 как было изначально)
    col_width = max(15, max_word_len + 2, max_count_len + 2)
    
    k = 0
    print(f'{"слово:":^{col_width}} |{"частота":^{col_width}}')
    print(f"{'-' * col_width}-|-{'-' * col_width}")
    for word, counts in dict_words_sort:
        if k == 5:
            break
        k += 1
        print(f'{word:^{col_width}} |{counts:^{col_width}}')

script()