from dataclasses import dataclass
from datetime import datetime, date

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        if not isinstance(self.fio, str):
            raise TypeError("ФИО должно быть строкой")
        if not isinstance(self.birthdate, str):
            raise TypeError("Дата рождения должно быть строкой в формате YYYY-MM-DD.")
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise TypeError("Неверный формат даты, введите в виде YYYY-MM-DD")
        if not isinstance(self.group, str):
            raise TypeError("Номер группы должен быть строкой")
        if isinstance(self.gpa, int):
            self.gpa = float(self.gpa)
        if not isinstance(self.gpa, float):
            raise TypeError("GPA должно быть числом с плавающей точкой")
        if not (0.0 <= self.gpa <= 5.0):
            raise ValueError("gpa должен быть от 0 до 5")
        
    def age(self) -> int:
        try:
            birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Неправильный формат даты: {self.birthdate}")
        
        today = date.today()
        age = today.year - birth_date.year
        
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1 # если ДР еще не наступил
        return age

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, d: dict):
        required_fields = ["fio", "birthdate", "group", "gpa"]
        
        for field in required_fields:
            if field not in d:
                raise ValueError(f"Missing required field: {field}")
        
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=d["gpa"]
        )

    def __str__(self):
        return f"Student: {self.fio}, Group: {self.group}, GPA: {self.gpa}, Age: {self.age()}"
    
# простой тест
if __name__ == "__main__":
    student = Student(
        fio="Тестовый Студент Николай",
        birthdate="2000-01-01", 
        group="TEST-01",
        gpa=4.5
    )
    print(student)
