import pytest, os
from lib import *


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
        ("   ", ""),
    ],
)
def test_normalize(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello world test", ["hello", "world", "test"]),
        ("", []),
        ("   ", []),
        ("знаки, препинания! тест.", ["знаки", "препинания", "тест"]),
    ],
)
def test_tokenize(text, expected):
    assert tokenize(text) == expected


def test_count_freq_basic():
    tokens = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    result = count_freq(tokens)
    expected = {"apple": 3, "banana": 2, "cherry": 1}
    assert result == expected


def test_count_freq_empty():
    assert count_freq([]) == {}


def test_top_n_basic():
    freq = {"apple": 5, "banana": 3, "cherry": 7, "date": 1}
    result = top_n(freq, 2)
    expected = [("cherry", 7), ("apple", 5)]
    assert result == expected


def test_top_n_tie_breaker():
    freq = {"banana": 3, "apple": 3, "cherry": 3}
    result = top_n(freq, 3)
    expected = [("apple", 3), ("banana", 3), ("cherry", 3)]
    assert result == expected


def test_top_n_empty():
    assert top_n({}, 5) == []


def test_full_pipeline():
    text = "Привет мир! Привет всем. Мир прекрасен."
    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)
    top_words = top_n(freq, 2)

    assert normalized == "привет мир! привет всем. мир прекрасен."
    assert tokens == [
        "привет",
        "мир",
        "привет",
        "всем",
        "мир",
        "прекрасен",
    ]
    assert freq == {"привет": 2, "мир": 2, "всем": 1, "прекрасен": 1}
    assert top_words == [("мир", 2), ("привет", 2)]


def test_table_output(capsys):
    """Тест для функции table_output"""
    text = "привет мир привет тест"
    table_output(text, top=2)

    captured = capsys.readouterr()
    output = captured.out

    assert "Всего слов: 4" in output
    assert "Уникальных слов: 3" in output
    assert "Топ 2:" in output
    assert "привет" in output


def test_json_to_csv_wrong_extension(tmp_path):
    """Тест на неверное расширение JSON файла"""
    src = tmp_path / "test.txt"
    dst = tmp_path / "test.csv"
    src.write_text("[]", encoding="utf-8")

    with pytest.raises(TypeError):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_not_list(tmp_path):
    """Тест JSON не являющегося списком"""
    src = tmp_path / "test.json"
    dst = tmp_path / "test.csv"
    src.write_text('{"key": "value"}', encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_not_dict_elements(tmp_path):
    """Тест JSON с элементами не-словарями"""
    src = tmp_path / "test.json"
    dst = tmp_path / "test.csv"
    src.write_text("[1, 2, 3]", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_csv_to_xlsx_basic(tmp_path):
    """Тест конвертации CSV в XLSX"""
    src = tmp_path / "test.csv"
    dst = tmp_path / "test.xlsx"

    content = "name,age\nAlice,22\nBob,25"
    src.write_text(content, encoding="utf-8")

    csv_to_xlsx(str(src), str(dst))

    # Проверяем что файл создался
    assert dst.exists()


def test_csv_to_xlsx_wrong_extension(tmp_path):
    """Тест неверного расширения для CSV"""
    src = tmp_path / "test.txt"
    dst = tmp_path / "test.xlsx"
    src.write_text("name,age\nAlice,22\n", encoding="utf-8")

    with pytest.raises(TypeError):
        csv_to_xlsx(str(src), str(dst))


def test_csv_to_xlsx_empty_file(tmp_path):
    """Тест пустого CSV файла"""
    src = tmp_path / "test.csv"
    dst = tmp_path / "test.xlsx"
    src.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        csv_to_xlsx(str(src), str(dst))


def test_ensure_directory_exists(tmp_path):
    """Тест создания директории"""
    # Импортируем функцию напрямую
    from lib.text import ensure_directory_exists

    test_dir = tmp_path / "new_dir" / "subdir"
    test_file = test_dir / "test.txt"

    ensure_directory_exists(str(test_file))

    assert test_dir.exists()


def test_is_file_empty(tmp_path):
    """Тест проверки пустого файла"""
    # Импортируем функцию напрямую
    from lib.text import is_file_empty

    empty_file = tmp_path / "empty.txt"
    empty_file.write_text("")

    non_empty_file = tmp_path / "non_empty.txt"
    non_empty_file.write_text("content")

    assert is_file_empty(str(empty_file)) == True
    assert is_file_empty(str(non_empty_file)) == False
