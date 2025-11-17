import string, os, sys
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    s = text
    if casefold:
        s = s.casefold()
    if yo2e:
        s = s.replace('ё', 'е').replace('Ё', 'Е')
    s = s.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    s = s.strip()
    while '  ' in s:
        s = s.replace('  ', ' ')
    return s

def tokenize(text: str) -> list[str]:
    s = text
    cyrillic_lower_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alp = cyrillic_lower_letters + string.ascii_lowercase + string.digits
    for i in range(len(s)):
        if s[i] in alp:
            continue
        else:
            s = s[:i] + ' ' + s[i+1:]
    while '  ' in s:
        s = s.replace('  ', ' ')
    s = s.split()
    return s

def count_freq(tokens: list[str]) -> dict[str, int]:
    d = {}
    tokens_set = set(tokens)
    for key in tokens_set:
        d[key] = tokens.count(key)
    return d

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    d = freq
    d = sorted(d.items(), key = lambda para: (-para[1], para[0]))
    return d

def ensure_directory_exists(file_path: str) -> None:
    """Создает директорию для файла, если она не существует"""
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

try:
    from src.lab03.text import normalize, tokenize, count_freq, top_n
except ImportError as e:
    sys.exit(f"Ошибка импорта: {e}")

def table_output(text: str):
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