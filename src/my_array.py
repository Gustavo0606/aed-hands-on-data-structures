from src.array import Array


class MyArray(Array):
    """
    Implementação concreta do TAD Array.
    """

    def __init__(self) -> None:
        self.data: list[int] = []

    def append(self, value: int) -> None:
        self.data.append(value)

    def get(self, index: int) -> int:
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError

    def set(self, index: int, value: int) -> None:
        if 0 <= index < len(self.data):
            self.data[index] = value
        else:
            raise IndexError

    def remove(self, value: int) -> None:
        naoEncontrado = True
        for i in range(len(self.data)):
            if self.data[i] == value:
                self.data.pop(i)
                naoEncontrado = False
                break
        if naoEncontrado:
            raise ValueError

    def insert(self, index: int, value: int) -> None:
        if 0 <= index <= len(self.data):
            self.data.insert(index, value)
        else:
            raise IndexError

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, index: int) -> int:
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError

    def __setitem__(self, index: int, value: int) -> None:
        if 0 <= index < len(self.data):
            self.data[index] = value
        else:
            raise IndexError

    def __repr__(self) -> str:
        return str(self.data)
