"""
Демонстрационная программа для чтения FASTA-файлов.

Программа считывает FASTA-записи с помощью класса FastaReader
и выводит заголовок, первые 100 символов последовательности,
её длину и предполагаемый тип алфавита.
"""
from collections.abc import Generator

from fasta_reader import FastaReader
from seq import Seq

def main() -> None:
    """
    Запускает демонстрационную программу для чтения FASTA-файлов.

    Запрашивает путь к файлу, последовательно обрабатывает FASTA-записи
    и выводит заголовок, первые 100 символов последовательности,
    её длину и предполагаемый тип алфавита.

    Обрабатывает ошибки чтения файла и некорректных входных данных.
    """
    try:
        reader: FastaReader = FastaReader(input("Введите путь к FASTA-файлу: "))
        records: Generator[Seq, None, None] = reader.fasta_reader()

        for record in records:
            print(record.seq_id)
            print(record.seq[:100])
            print(len(record))
            print(record.alphabet())

    except FileNotFoundError as error:
        print(f"Не удалось найти FASTA-файл: {error.filename}")

    except TypeError as error:
        print(error)

    except ValueError as error:
        print(error)
        print("Обработка FASTA-файла прервана из-за ошибки формата.")


if __name__ == "__main__":
    main()

