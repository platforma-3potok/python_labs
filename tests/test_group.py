# run_lab9.py
import sys
import os

# Добавляем путь для импортов
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.lab09 import Group
from src.lab08.models import Student

def main():
    print('\n' + "ЗАПУСК ЛАБОРАТОРНОЙ РАБОТЫ 9")
    print("=" * 50)
    
    # Указываем путь к вашему CSV-файлу
    csv_file = "../data/lab09/students.csv"
    print(f"📁 Используем файл: {csv_file}")
    
    # Создаём объект Group
    group = Group(csv_file)
    
    # БЕСКОНЕЧНЫЙ ЦИКЛ МЕНЮ
    while True:
        print("\n" + "=" * 50)
        print("📋 МЕНЮ ДОСТУПНЫХ МЕТОДОВ:")
        print("1. 📝 list() - показать всех студентов")
        print("2. ➕ add() - добавить студента")
        print("3. 🔍 find() - найти студента по подстроке")
        print("4. ✏️ update() - обновить данные студента")
        print("5. 🗑️ remove() - удалить студента")
        print("6. 📊 stats() - статистика по группе")
        print("7. ❌ Выход")
        print("=" * 50)
        
        choice = input("\nВыберите действие (1-7): ").strip()
        
        if choice == "1":
            # list()
            print("\n📋 СПИСОК ВСЕХ СТУДЕНТОВ:")
            students = group.list()
            if not students:
                print("   Нет студентов")
            else:
                for i, student in enumerate(students, 1):
                    print(f"{i:3}. {student.fio:30} | Группа: {student.group:10} | GPA: {student.gpa:.1f}")
        
        elif choice == "2":
            # add()
            print("\n➕ ДОБАВЛЕНИЕ НОВОГО СТУДЕНТА:")
            try:
                fio = input("ФИО: ").strip()
                birthdate = input("Дата рождения (ГГГГ-ММ-ДД): ").strip()
                group_name = input("Группа: ").strip()
                gpa = float(input("GPA (0.0-5.0): ").strip())
                
                student = Student(
                    fio=fio,
                    birthdate=birthdate,
                    group=group_name,
                    gpa=gpa
                )
                group.add(student)
                print("✅ Студент добавлен!")
            except Exception as e:
                print(f"❌ Ошибка: {e}")
        
        elif choice == "3":
            # find()
            print("\n🔍 ПОИСК СТУДЕНТА:")
            substr = input("Введите подстроку для поиска в ФИО: ").strip()
            result = group.find(substr)
            
            if isinstance(result, list):
                if not result:
                    print(f"❌ Студенты с '{substr}' не найдены")
                else:
                    print(f"✅ Найдено {len(result)} студентов:")
                    for i, student in enumerate(result, 1):
                        print(f"{i}. {student.fio} - {student.group} - GPA: {student.gpa:.1f}")
            else:
                print(result)
        
        elif choice == "4":
            # update()
            print("\n✏️ ОБНОВЛЕНИЕ ДАННЫХ СТУДЕНТА:")
            fio = input("ФИО студента для обновления: ").strip()
            
            print("Какие поля обновить? (оставьте пустым, если не менять)")
            new_fio = input(f"Новое ФИО [{fio}]: ").strip() or None
            new_birthdate = input("Новая дата рождения: ").strip() or None
            new_group = input("Новая группа: ").strip() or None
            new_gpa_input = input("Новый GPA: ").strip()
            new_gpa = float(new_gpa_input) if new_gpa_input else None
            
            # Собираем поля для обновления
            fields = {}
            if new_fio: fields['fio'] = new_fio
            if new_birthdate: fields['birthdate'] = new_birthdate
            if new_group: fields['group'] = new_group
            if new_gpa is not None: fields['gpa'] = new_gpa
            
            if fields:
                result = group.update(fio, **fields)
                print(f"✅ {result}")
            else:
                print("❌ Не указано ни одного поля для обновления")
        
        elif choice == "5":
            # remove()
            print("\n🗑️ УДАЛЕНИЕ СТУДЕНТА:")
            fio = input("Введите ФИО студента для удаления: ").strip()
            result = group.remove(fio)
            print(f"✅ {result}")
        
        elif choice == "6":
            # stats()
            print("\n📊 СТАТИСТИКА ПО ГРУППЕ:")
            stats = group.stats()
            print(f"Всего студентов: {stats['count']}")
            print(f"Минимальный GPA: {stats['min_gpa']:.2f}")
            print(f"Максимальный GPA: {stats['max_gpa']:.2f}")
            print(f"Средний GPA: {stats['avg_gpa']:.2f}")
            
            print("\nРаспределение по группам:")
            for group_name, count in stats['groups'].items():
                print(f"  {group_name}: {count} студентов")
            
            print("\nТоп-5 студентов по GPA:")
            for i, student in enumerate(stats['top_5_students'], 1):
                print(f"  {i}. {student.fio}: {student.gpa:.1f}")
        
        elif choice == "7":
            print("\n👋 Выход из программы")
            break
        
        else:
            print("❌ Неверный выбор. Попробуйте снова.")
        
        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()