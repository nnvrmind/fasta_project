from collections.abc import Generator
from seq import Seq

class FastaReader:
    """
    Класс для построчного чтения и проверки файлов формата FASTA.

    Parameters
    ----------
    path : str
        Путь к FASTA-файлу.

    Attributes
    ----------
    path : str
        Путь к FASTA-файлу.
    """

    def __init__(self, path: str) -> None:
        """
        Инициализирует экземпляр класса FastaReader.

        Parameters
        ----------
        path : str
            Путь к FASTA-файлу.
        """
        self.path: str = path

    def fasta_reader(self) -> Generator[Seq, None, None]:
        """
        Читает FASTA-файл построчно и последовательно выдаёт объекты Seq.

        Yields
        ------
        Seq
            Объект, содержащий заголовок и биологическую
            последовательность одной FASTA-записи.

        Raises
        ------
        FileNotFoundError
            Если файл по указанному пути не найден.
        ValueError
            Если FASTA-файл пустой, отсутствует начальный символ '>'
            или одна из FASTA-записей не содержит последовательности.
        """
        with open(self.path) as file:

            first_symbol: str = file.read(1)
            if not first_symbol:
                raise ValueError("FASTA-файл пустой.")
            if first_symbol != ">":
                raise ValueError("Некорректная FASTA-запись, отсутствует начальный символ '>'.")
            file.seek(0)

            seq_id: str = ""
            seq: list[str] = []
            for line in file:
                if not line.strip():
                    continue
                elif line[0] == ">":
                    if seq_id:
                        if not seq:
                            raise ValueError(f"Некорректная FASTA-запись, отсутствует "
                                             f"последовательность у заголовка {seq_id}.")
                        yield Seq(seq_id, "".join(seq))
                    seq_id = line.strip()
                    seq.clear()
                else:
                    seq.append(line.strip())

            # проверка для последней биологической последовательности в файле
            if seq_id and seq:
                yield Seq(seq_id, "".join(seq))
            elif seq_id and (not seq):
                raise ValueError("Некорректная FASTA-запись, отсутствует последовательность.")




