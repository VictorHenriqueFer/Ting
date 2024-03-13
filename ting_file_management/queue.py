from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._files = []

    def __len__(self):
        return len(self._files)

    def enqueue(self, v):
        self._files.append(v)

    def dequeue(self):
        if self.__len__() > 0:
            return self._files.pop(0)
        else:
            raise IndexError("Fila Vazia")

    def search(self, x):
        if x >= 0 and x < self.__len__():
            return self._files[x]
        else:
            raise IndexError("Índice Inválido ou Inexistente")
