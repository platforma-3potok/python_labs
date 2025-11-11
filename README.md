Cтудент группы БИВТ-25-8 Ищейкин Кирилл Алексеевич
# Лабораторные работы

## Лабораторная работа №1

---

- ###  1 задание
#### Код
```python
Name = input('Введите имя:')
Age = int(input('Введите возраст:'))
print(f'Привет, {Name}! Через год тебе будет {Age+1}.')
```
#### Вывод
![](images/lab01/image_1.png)

---

- ### 2 задание
#### Код  
```python
a = input()
b = input()
a = float(a.replace(',', '.'))
b = float(b.replace(',', '.'))
avg = round((a + b)/ 2, 2)
sumi = a + b
print(sumi, avg, sep='; ')
```
#### Вывод
![](images/lab01/image_2.png)

---

- ### 3 задание
#### Код
```python
price= int(input())
discount= int(input())
vat= int(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {round(base, 2)} ₽')
print(f'НДС: {round(vat_amount, 2)} ₽')
print(f'Итого к оплате: {round(total, 2)} ₽')
```
#### Вывод
![](images/lab01/image_3.png)

---

- ###  4 задание
#### Код  
```python
m = int(input())
h = m // 60
hm = m % 60
print(f'{h}:{hm:02d}')
```
#### Вывод
![](images/lab01/image_4.png)

---

- ###  5 задание
#### Код  
```python
FCS = input()
initials = ''
len_FCS = len(FCS)
k = len_FCS - FCS.count(' ')
if FCS[0] != ' ':
	initials += FCS[0]
for i in range(1, len_FCS):
	if FCS[i] != ' ' and FCS[i-1] == ' ':
		initials += FCS[i]
print(initials)
print(k+2)
```
#### Вывод
![](images/lab01/image_5.png)

---

- ###  6 задание
#### Код  
```python
N = int(input())
list_student = []
for i in range(N):
	student = input('')
	student = student.split()
	list_student.append(student)
koch = 0
kzaoch = 0
for i in range(N):
	if list_student[i][-1] == 'True':
		format = True
	else:
		format = False
	if format:
		koch += 1
	else:
		kzaoch += 1
print(koch, kzaoch)
```
#### Вывод
![](images/lab01/image_6.png)

---

- ###  7 задание
#### Код  
```python
s = input()
len_s = len(s)
out_s = ''
num = '0123456789'
for i in range(len_s):
	if s[i].upper() == s[i]:
		first_ind = i
		break
for i in range(first_ind, len_s):
	if s[i] in num:
		second_ind = i + 1
		break
d = second_ind - first_ind
for i in range(first_ind, len_s, d):
	out_s += s[i]
print(out_s)
```
#### Вывод
![](images/lab01/image_7.png)

---

## Лабораторная работа №2

---

- ###  задание A
#### Код
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("Список пустой")
    maxi = max(nums)
    mini = min(nums)
    return mini, maxi

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    list_sorted = sorted(set(nums))
    return list_sorted

def flatten(mat: list[list | tuple]) -> list:
    res = []
    for x in mat:
        if not isinstance(x, (list, tuple)):
            raise TypeError('строка не строка строк матрицы')
        for y in x:
            res.append(y)
    return res

example_list_1 = [-3.1, 2]
example_list_2 = [1.0, 1, 2.5, 2.5, 0]
example_list_3 = [[1], [], [2, 3]]

result_1 = min_max(example_list_1)
result_2 = unique_sorted(example_list_2)
result_3 = flatten(example_list_3)

print(f'Результат команды min_max: {result_1}')
print(f'Результат команды unique_sorted: {result_2}')
print(f'Результат команды flatten: {result_3}')
```
#### Вывод
![](images/lab02/image_arrays.png)

---

- ###  задание B
#### Код
```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    len_mat = len(mat)
    if len_mat == 0:
        return []
    len_row = len(mat[0])

    if any(len(row) != len_row for row in mat):
        raise ValueError("рваная матрица")
    
    new_mat = [ [ [] for y in range(len_mat) ] for x in range(len_row)]
    
    for i in range(len_mat):
        for j in range(len_row):
            new_mat[j][i] = mat[i][j]

    return new_mat

def row_sums(mat: list[list[float | int]]) -> list[float]:
    len_mat = len(mat)
    if len_mat == 0:
        return []
    len_row = len(mat[0])

    if any(len(row) != len_row for row in mat):
        raise ValueError("рваная матрица")    
    
    res = [sum(x) for x in mat]

    return res

def col_sums(mat: list[list[float | int]]) -> list[float]:
    len_mat = len(mat)
    if len_mat == 0:
        return []
    len_row = len(mat[0])
    
    if any(len(row) != len_row for row in mat):
        raise ValueError("рваная матрица")   
    
    res = [[] for x in range(len_row)]
    for i in range(len_mat):
       res[i] = sum([mat[j][i] for j in range(len_row)])
    return res

exmaple_mat_1 = [[1, 2], [3, 4]]
exmaple_mat_2 = [[1, 2, 3], [4, 5, 6]]
exmaple_mat_3 = [[-1, 1], [10, -10]]

result_1 = transpose(exmaple_mat_1)
result_2 = row_sums(exmaple_mat_2)
result_3 = col_sums(exmaple_mat_3)

print(f'Результат команды transpose: {result_1}')
print(f'Результат команды row_sums: {result_2}')
print(f'Результат команды col_sums: {result_3}')
```
#### Вывод
![](images/lab02/image_matrix.png)

---

- ###  задание C
#### Код
```python
def fio_to_fcs(fio: str):
    fio = fio.strip()
    fcs = ''
    len_fio = len(fio)
    k = 0
    while fio[k] != ' ':
        fcs += fio[k]
        k += 1
    fcs = fcs.capitalize()
    fcs += ' '
    for i in range(k, len_fio):
        if fio[i] != ' ' and fio[i-1] == ' ':
            fcs += fio[i].upper() + '.'
    return fcs

def format_record(rec: tuple[str, str, float]) -> str:
    fio: str = rec[0]
    group: str = rec[1]
    gpa: float = rec[2]

    if len(fio) == 0 or all(x == ' ' for x in fio):
        raise ValueError('Пустое ФИО')
    if len(group) == 0 or all(x == ' ' for x in group):
        raise ValueError('Пустая группа')
    if not isinstance(gpa, float):
        raise TypeError('неверный тип GPA')
    
    fcs = fio_to_fcs(fio)
    group = f'гр. {group}'
    gpa = f'{gpa: .2f}'

    print(f'{fcs}, {group}, GPA {gpa}')

format_record( ("  сидорова  анна   сергеевна ", "ABB-01", 3.999) )
```
#### Вывод
![](images/lab02/image_tuples.png)

---

## Лабораторная работа №3

---

- ###   задание A
#### Код
```python
import string
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


example_normalize = "  двойные   пробелы  "
example_tokenize = "emoji 😀 не слово"
example_count_freq = ["bb","aa","bb","aa","cc"]

res_normalise = normalize(example_normalize)
res_tokenize = tokenize(example_tokenize)
res_count_freq = count_freq(example_count_freq)
res_count_top_n = top_n(res_count_freq)

print(res_normalise)    
print(res_tokenize)
print(res_count_freq)
print(res_count_top_n)
```
#### Вывод
![](images/lab03/image_text_py.png)

---

- ###   задание B
#### Код
```python
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
    k = 0
    print(f'{"слово:":^15} |{"частота":^15}')
    print(f"{'----------'*3:^30}")
    for word, counts in dict_words_sort:
        if k == 5:
            break
        k += 1
        print(f'{word:^15} |{counts:^15}')

script()
```
#### Вывод
![](images/lab03/text_stats_py.png)

---

## Лабораторная работа №4

---

- ###   задание A
#### Код
```python

import csv
from pathlib import Path
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    with open(path, 'r', encoding=encoding) as f:
        return f.read()

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    if rows and len(set(len(row) for row in rows)) != 1:
        raise ValueError("Все строки должны иметь одинаковую длину")
    
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        writer.writerows(rows)

if __name__ == "__main__":
    try:
        txt = read_text('src\lab04\Text.txt')
        print(f"Прочитано: {txt}")
    except FileNotFoundError:
        print("Файл text.txt не найден")
    
    write_csv([("word", "count"), ("test", 3)], "table.csv")  
    print("файл csv создан!")

```
#### Вывод
![](images\lab04\io_txt_csv_A.png)

---

- ###   задание B
#### Код
```python

import sys, os, csv
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

try:
    from src.lab03.text import normalize, tokenize
except ImportError as e:
    sys.exit(f"Ошибка импорта: {e}")

def main():
    input_file = 'src\lab04\Text.txt'
    output_file = 'src\lab04\Table.csv'

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
        if not text.strip():
            sys.exit("Файл пустой")
    except Exception as e:
        sys.exit(f"Ошибка чтения {input_file}: {e}")
    
    try:
        normalized = normalize(text)
        words = tokenize(normalized)
        if not words:
            sys.exit("После обработки слов не найдено")
        word_freq = Counter(words)
    except Exception as e:
        sys.exit(f"Ошибка обработки текста: {e}")


    try:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['word', 'count'])
            for word, count in sorted(word_freq.items(), key=lambda x: (-x[1], x[0])):
                writer.writerow([word, count])
    except Exception as e:
        sys.exit(f"Ошибка сохранения {output_file}: {e}")
    
    top5 = sorted(word_freq.items(), key=lambda x: (-x[1], x[0]))[:5]
    print(f"Всего слов: {len(words)}")
    print(f"Уникальных слов: {len(word_freq)}")
    print('Топ 5:')
    k = 0
    print(f'{"слово:":^15} |{"частота":^15}')
    print(f"{'----------'*3:^30}")
    for word, counts in top5:
        if k == 5:
            break
        k += 1
        print(f'{word:^15} |{counts:^15}')

if __name__ == "__main__":
    main()

```
#### Вывод
![](images\lab04\io_txt_csv_B.png)

---

## Лабораторная работа №5

---

- ###   задание A
#### Код
```python
import csv, json, os, sys
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.func1 import is_file_empty
from lib.text import ensure_directory_exists
def json_to_csv(json_path: str, csv_path: str) -> None:
	# Проверка json файла
	json_file = Path(json_path)
	if not json_file.exists():
		raise FileNotFoundError(f'JSON файл не найден: {json_path}')
	
	if json_file.suffix.lower() != '.json':
		raise TypeError(f'Файл должен быть в формате json')
	
	if is_file_empty(json_path):
		raise FileNotFoundError(f'Файл {json_path} пустой')
	
	ensure_directory_exists(csv_path)
	# Проверка csv файла
	try:
		csv_file = Path(csv_path)
	except:
		raise FileNotFoundError(f'csv файл не найден: {csv_path}')
	if csv_file.suffix.lower() != '.csv':
		raise TypeError(f'Файл должен быть в формате csv')
	
	try:
		with open(json_path, 'r' ,encoding='utf-8') as json_file:
			data = json.load(json_file)
	except json.JSONDecodeError as e:
		raise ValueError(f'Ошибка парсинга JSON: {e}')
	
	# Проверяем, что json состоит из списков
	if not isinstance(data, list):
		raise ValueError("JSON должен содержать список объектов")
	
	# Проверяем структуры данных
	if not all(isinstance(item, dict) for item in data):
		raise ValueError("Все элементы в JSON должны быть словарями")
	
	fieldnames = set()
	for item in data:
		fieldnames.update(item.keys())
	
	try:
		with open(csv_path, 'w' ,encoding='utf-8', newline='') as csv_file:
			writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

			writer.writeheader()

			for item in data:
				row = {key: item.get(key, '') for key in fieldnames}
				writer.writerow(row)
	except Exception as e:
		raise ValueError(f"Ошибка записи CSV: {e}")


def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_file = Path(csv_path)
    ensure_directory_exists(json_path)
    json_file = Path(json_path)
    
    try:
        data = []     
        with open(csv_file, 'r', encoding='utf-8') as f:
			# Проверяем заголовки 
            sample = f.read(1024)
            f.seek(0)
            sniffer = csv.Sniffer()
            try:            
                has_header = sniffer.has_header(sample)
            except csv.Error:
                has_header = True           
            if not has_header:
                raise ValueError("CSV файл, вероятно, не содержит заголовок (эвристический подход)")	
			
            # Пытаемся прочитать CSV с заголовками
            csv_reader = csv.DictReader(f)
            
            # Проверяем, есть ли поле fieldnames (заголовки)
            if csv_reader.fieldnames is None:
                raise ValueError("CSV файл не содержит заголовков!")
            # Проверяем, что все заголовки уникальны
            if len(csv_reader.fieldnames) != len(set(csv_reader.fieldnames)):
                raise ValueError("Заголовки CSV содержат дубликаты!")
            
            # Читаем данные
            for row in csv_reader:
                data.append(row)
        
        # Сохраняем JSON
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
    except Exception as e:
        print(f"Ошибка: {e}")

try:
	json_to_csv("python_labs/data/samples/empty_json.json", "python_labs/data/out/empty_json.csv")
	csv_to_json("python_labs/data/samples/no_header_csv.csv", "python_labs/data/out/no_header_csv.json")
	json_to_csv("python_labs/data/samples/test_missing_fields.json", "python_labs/data/out/missing_fields_from_json.csv")
	json_to_csv("python_labs/data/samples/people.json", "python_labs/data/out/people_from_json.csv")
	csv_to_json("python_labs/data/samples/people.csv", "python_labs/data/out/people_from_csv.json")
except Exception as e:
     print(f"Ошибка: {e}")

```
#### Вывод
пустый json
![](python_labs\images\lab05\empty_json.png)
csv без заголовков не создает json файл
![](python_labs\images\lab05\no_logo.png)
people csv -> json
![](python_labs\images\lab05\people_json.png)
people json -> csv
![](python_labs\images\lab05\people_csv.png)
пустые ячейки
![](python_labs\images\lab05\missing.png)
---

- ###   задание B
#### Код
```python
import openpyxl, os, sys, csv
from pathlib import Path
from openpyxl.utils import get_column_letter

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from lib.func1 import is_file_empty

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    # Добавляем путь csv и xlsx файла
    csv_file = Path(csv_path)
    xlsx_file = Path(xlsx_path)
    
    # Проверяем существует ли файл
    if not csv_file.exists():
        raise FileNotFoundError(f'Файл {csv_path} не найден')
    
    # Проверяем пустой файл или нет
    if is_file_empty(csv_file):
        raise ValueError(f'Файл {csv_path} пустой')
    
    # Проверяем формат файлов
    if csv_file.suffix.lower() != '.csv':
        raise TypeError(f'файл {csv_path} не формата csv')

    # Создаем директорию для XLSX файла если её нет
    xlsx_file.parent.mkdir(parents=True, exist_ok=True)

    # Читаем CSV и конвертируем в XLSX
    try:
        # Создаем новую книгу Excel
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = "Sheet1"

        with open(csv_file, 'r', encoding='utf-8', newline='') as file:
            csv_reader = csv.reader(file)

            # При помощи циклов записываем данные в xlsx
            for row_idx, row in enumerate(csv_reader, 1):
                for col_idx, value in enumerate(row, 1):
                    worksheet.cell(row=row_idx, column=col_idx, value=value)

        # Задаем ширину колонок
        for column in worksheet.columns:
            max_length = 0
            column_letter = get_column_letter(column[0].column) 
            
            for cell in column:
                if cell.value:  # Проверяем что значение не None
                    cell_length = len(str(cell.value))
                    if cell_length > max_length:
                        max_length = cell_length
            
            # Устанавливаем ширину колонки (не менее 8 символов)
            column_width = max(max_length + 2, 8)
            worksheet.column_dimensions[column_letter].width = column_width

        # Сохраняем файл
        workbook.save(xlsx_file)
        print(f"Успешно создан XLSX файл: {xlsx_path}")
        
    except Exception as e:
        raise ValueError(f'Не получилось считать CSV файл: {e}')

try:
    csv_to_xlsx("python_labs/data/samples/people.csv", "python_labs/data/out/people.xlsx")
    csv_to_xlsx("python_labs/data/samples/cities.csv", "python_labs/data/out/cities.xlsx")  
except Exception as e:
    print(f"Ошибка: {e}")
```
#### Вывод
cities.xlsx
![](python_labs\images\lab05\cities_xlsx.png)
people.xlsx
![](python_labs\images\lab05\people_xlsx.png)

---