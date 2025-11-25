def fio_to_fcs(fio: str):
    fio = fio.strip()
    fcs = ""
    len_fio = len(fio)
    k = 0
    while fio[k] != " ":
        fcs += fio[k]
        k += 1
    fcs = fcs.capitalize()
    fcs += " "
    for i in range(k, len_fio):
        if fio[i] != " " and fio[i - 1] == " ":
            fcs += fio[i].upper() + "."
    return fcs


def format_record(rec: tuple[str, str, float]) -> str:
    if not isinstance(rec, tuple):
        raise TypeError("не кортеж")
    if len(rec) != 3:
        raise ValueError("неверная длина кортежа")
    if len(fio) == 0 or all(x == " " for x in fio):
        raise ValueError("Пустое ФИО")
    if len(group) == 0 or all(x == " " for x in group):
        raise ValueError("Пустая группа")
    if not isinstance(gpa, float):
        raise TypeError("неверный тип GPA")

    fio: str = rec[0]
    group: str = rec[1]
    gpa: float = rec[2]

    fcs = fio_to_fcs(fio)
    group = f"гр. {group}"
    gpa = f"{gpa: .2f}"

    print(f"{fcs}, {group}, GPA {gpa}")


format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999))
