import csv
from src.lab08.models import Student
from pathlib import Path


class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()
        
    def _ensure_storage_exists(self):
        """Создаёт CSV-файл с заголовками, если его нет"""
        if not self.path.exists():
            # Создаём папки если их нет
            self.path.parent.mkdir(parents=True, exist_ok=True)
            
            # Создаём файл и пишем заголовок
            with open(self.path, 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["fio", "birthdate", "group", "gpa"])

    def add(self, student: Student):
        with open(self.path, 'a', newline='') as file:
            writer = csv.writer(file)

            row_data = [
                student.fio,
                student.birthdate,
                student.group,
                str(student.gpa)
            ]
            writer.writerow(row_data)

            print(f"Добавлен студент {student.fio}")

    def list(self):
        return self._read_all()

    def _read_all(self):
        """Вернёт список объектов Student"""
        if not self.path.exists():
            return []
        
        students = []
        with open(self.path, 'r', encoding='utf-8', newline='') as file:
            reader = csv.DictReader(file)  

            for row_dict in reader:  
                student = Student.from_dict(row_dict)  
                students.append(student)

        return students
    
    def _write_all(self, students: list[Student]):
        with open(self.path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["fio", "birthdate", "group", "gpa"])

            for student in students:
                row_data = [
                    student.fio,
                    student.birthdate,
                    student.group,
                    str(student.gpa)
                ]

                writer.writerow(row_data)
    
    def find(self, substr: str):
        students = self._read_all()
        found_students = []
        for student in students:
            if student.fio.lower() == substr.lower():
                found_students.append(student)
        if len(found_students) == 0:
            return f"Студент {substr} не найден"
        return found_students
    
    def remove(self, fio: str):
        students = self._read_all()
        all_students = []
        for student in students:
            if student.fio.lower() != fio.lower():
                all_students.append(student)

        kb = len(students)
        ka = len(all_students)
        if kb != ka:
            self._write_all(all_students)
            return f'студент {fio} успешно удален'
        else:
            return f'Cтудент {fio} не найден'
        
    def update(self, fio: str, **fields):
        students = self._read_all()
        field_fio = fields.get('fio')
        field_birthdate = fields.get('birthdate')
        field_group = fields.get('group')
        field_gpa = fields.get('gpa')
        all_students = []
        student_found = False
        for student in students:
            if student.fio.lower() != fio.lower():
                all_students.append(student)
            else:
                student_found = True
                if field_fio is not None:
                    student.fio = field_fio
                if field_birthdate is not None:
                    student.birthdate = field_birthdate
                if field_group is not None:
                    student.group = field_group
                if field_gpa is not None:
                    student.gpa = field_gpa
        if student_found: return f'Студент {fio} не найден'
        self._write_all(all_students)
        return f'Данные студента {fio} изменены'