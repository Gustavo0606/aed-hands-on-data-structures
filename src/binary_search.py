from src.my_array import MyArray


def binary_search(array: MyArray, target: int) -> int:
    """
    Realiza busca binária em um array ordenado.

    Deve retornar o índice do elemento ou -1 caso não encontrado.
    """
    left = 0
    right = (len(array)-1)
    while left <= right:
        meio = (left + right)//2
        if array[meio] == target:
            return meio
        elif array[meio] < target:
            left = meio + 1
        else:
            right = meio - 1
    return -1
