class Seq:
    """
    Класс для хранения и обработки биологических последовательностей в формате FASTA.

    Parameters
    ----------
    seq_id : str
        Заголовок FASTA-записи, передаваемый при создании объекта.
    seq : str
        Строка, содержащая биологическую последовательность.

    Attributes
    ----------
    seq_id : str
        Заголовок FASTA-записи, содержащий информацию о последовательности.
    seq : str
        Биологическая последовательность, представленная строкой символов.
    """

    def __init__(self, seq_id: str, seq: str) -> None:
        """
        Инициализирует экземпляр класса Seq.

        Raises
        ------
        TypeError
            Если переданные аргументы имеют некорректный тип.
        ValueError
            Если FASTA-заголовок пустой или не начинается с символа '>',
            либо биологическая последовательность пуста.
        """
        if not isinstance(seq_id, str):
            raise TypeError("FASTA-заголовок должен быть строкой.")
        if not isinstance(seq, str):
            raise TypeError("Биологическая последовательность должна быть строкой.")
        if not seq_id or seq_id[0] != ">":
            raise ValueError("Некорректный FASTA-заголовок.")
        if not seq:
            raise ValueError("Последовательность не может быть пустой.")

        self.seq_id: str= seq_id
        self.seq: str = seq

    def __str__(self) -> str:
        """
        Возвращает строковое представление FASTA-записи.

        Returns
        -------
        str
            Строка, содержащая FASTA-заголовок и биологическую
            последовательность, разделённые переносом строки.
        """
        return f"{self.seq_id}\n{self.seq}"

    def __len__(self) -> int:
        """
        Возвращает длину биологической последовательности.

        Returns
        -------
        int
            Длина последовательности.
        """
        return len(self.seq)

    def alphabet(self) -> str:
        """
        Определяет тип биологической последовательности по её алфавиту.

        Returns
        -------
        str
            Предполагаемый тип последовательности: нуклеотидная,
            белковая или последовательность с неизвестным алфавитом.
            При совпадении обоих алфавитов приоритет отдаётся
            нуклеотидной последовательности.
        """
        nucleotide_alphabet: str = "ACGTUN"
        protein_alphabet: str = "ACDEFGHIKLMNPQRSTVWYX"

        if all(i in nucleotide_alphabet for i in self.seq):
            return "Это нуклеотидная последовательность."

        elif all(i in protein_alphabet for i in self.seq):
            return "Это белковая последовательность."

        else:
            return "Последовательность с неизвестным алфавитом."

