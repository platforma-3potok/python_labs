import argparse
import sys
import os
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from lib.text import table_output


def stats(input_file: str, top: int = 5):
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read()

        table_output(text, top)

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден")
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")


# остальной код без изменений...
def cat(input_file: str, number_lines: bool = False):
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for i, line in enumerate(lines, 1):
            if number_lines:
                print(f"{i:6d}  {line}", end="")
            else:
                print(line, end="")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")


def main():
    parser = argparse.ArgumentParser(description="CLI утилиты")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество топ-слов")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == "stats":
        stats(args.input, args.top)
    elif args.command == "cat":
        cat(args.input, args.n)


if __name__ == "__main__":
    main()
