from __future__ import annotations
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
        with open(self.path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            row_data = [
                student.fio.title(),
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
        with open(self.path, 'w', newline='', encoding='utf-8') as file:
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
            if substr.lower() in student.fio.lower():
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
                all_students.append(student)
        if not student_found: return f'Студент {fio} не найден'
        self._write_all(all_students)
        return f'Данные студента {fio} изменены'
    
    def stats(self) -> dict:
        students = self._read_all()
        count_students = len(students)
        min_gpa = 5.0
        max_gpa = 0.0
        sum_gpa = 0
        csig = {} # count_students_in_group
        students = sorted(students, key = lambda student: (-student.gpa, student.fio))

        top_5_students = []
        k = 0
        for student in students:
            k += 1
            if k <= 5: top_5_students.append(student)

            t_gpa = float(student.gpa)
            sum_gpa += t_gpa
            if t_gpa > max_gpa:
                max_gpa = t_gpa
            if t_gpa < min_gpa:
                min_gpa = t_gpa
            
            t_group = student.group
            if t_group not in csig:
                csig[t_group] = 1
            else:
                csig[t_group] += 1
            
        avg_gpa = sum_gpa / count_students

        d = {
            "count": count_students,
            "min_gpa": min_gpa,
            "max_gpa": max_gpa,
            "avg_gpa": avg_gpa,
            "groups": csig,
            "top_5_students": top_5_students
        }
        
        return d