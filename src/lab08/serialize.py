import json
from typing import List
from models import Student
import os

def students_to_json(students: List[Student], path: str) -> None:
    if not isinstance(students, list):
        raise TypeError("Объект students должен быть типа list")
    if not isinstance(path, str):
        raise TypeError("Путь должен быть строкой")
    
    data = [student.to_dict() for student in students]

    os.makedirs(os.path.dirname(path), exist_ok=True)

    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"ошибка при при превращении в json {e}")
    except TypeError as e:
        raise TypeError(f"Ошибка сериализации JSON: {e}")
    
def students_from_json(path: str) -> List[Student]:
    if not isinstance(path, str):
        raise TypeError("Путь должен быть строкой")
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        students = []
        for item in data:
            try:
                student = Student.from_dict(item)
                students.append(student)
            except (ValueError, KeyError) as e:
                print(f"Ошибка при загрузке студента: {e}")
                continue
                
        return students
    except FileNotFoundError:
        print(f"Файл {path} не найден")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON")
        return []
def main():
    input_path = "python_labs/data/lab08/students_input.json"
    students = students_from_json(input_path)
    if students:
        print(f"Успешно загружено {len(students)} студентов:\n")
        for i, student in enumerate(students, 1):
            print(f"{i}. {student}")
    else:
        print("Ошибка при загрузке студентов")
        print(f"Файл {input_path} либо не существует, либо не содержит корректные данные")
if __name__ == "__main__":
    main() 
    