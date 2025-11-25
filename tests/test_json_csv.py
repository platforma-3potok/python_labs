import pytest
from lib import *
from pathlib import Path
import json
import csv


def write_json(path: Path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def read_csv_rows(path: Path):
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


# ПОЗИТИВНЫЕ СЦЕНАРИИ


def test_json_to_csv_roundtrip(tmp_path: Path):
    """Корректная конвертация JSON → CSV"""
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]
    write_json(src, data)

    json_to_csv(str(src), str(dst))
    rows = read_csv_rows(dst)

    # Проверяем количество записей и набор ключей
    assert len(rows) == 2
    assert set(rows[0].keys()) == {"name", "age"}
    assert rows[0]["name"] == "Alice"
    assert rows[1]["name"] == "Bob"


def test_csv_to_json_roundtrip(tmp_path: Path):
    """Корректная конвертация CSV → JSON"""
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"

    # Создаем CSV с заголовками
    with src.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age"])
        writer.writerow(["Alice", "22"])
        writer.writerow(["Bob", "25"])

    csv_to_json(str(src), str(dst))
    data = read_json(dst)

    # Проверяем количество записей и набор ключей
    assert isinstance(data, list)
    assert len(data) == 2
    assert set(data[0].keys()) == {"name", "age"}
    assert data[0]["name"] == "Alice"
    assert data[1]["name"] == "Bob"


# НЕГАТИВНЫЕ СЦЕНАРИИ


def test_json_to_csv_empty_file_raises(tmp_path: Path):
    """Пустой JSON файл → ValueError"""
    src = tmp_path / "empty.json"
    dst = tmp_path / "out.csv"
    src.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_malformed_json_raises(tmp_path: Path):
    """Некорректный JSON → ValueError"""
    src = tmp_path / "bad.json"
    dst = tmp_path / "out.csv"
    src.write_text("{ bad json", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_csv_to_json_empty_file_raises(tmp_path: Path):
    """Пустой CSV файл → ValueError"""
    src = tmp_path / "empty.csv"
    dst = tmp_path / "out.json"
    src.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        csv_to_json(str(src), str(dst))


def test_nonexistent_path_raises(tmp_path: Path):
    """Несуществующий файл → FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        json_to_csv(str(tmp_path / "no_such.json"), str(tmp_path / "out.csv"))

    with pytest.raises(FileNotFoundError):
        csv_to_json(str(tmp_path / "no_such.csv"), str(tmp_path / "out.json"))
