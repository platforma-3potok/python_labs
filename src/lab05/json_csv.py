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
