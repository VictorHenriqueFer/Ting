import pytest
from ting_file_management.priority_queue import PriorityQueue
baixo = {"nome_do_arquivo": "low_priority.txt", "qtd_linhas": 10}
baixoDois = {"nome_do_arquivo": "low_priority_2.txt", "qtd_linhas": 6}
aia = {"nome_do_arquivo": "priority.txt", "qtd_linhas": 1}
priDois = {"nome_do_arquivo": "priority_2.txt", "qtd_linhas": 1}


def test_basic_priority_queueing():
    xx = PriorityQueue()
    xx.enqueue(baixo)
    xx.enqueue(aia)
    xx.enqueue(baixoDois)
    xx.enqueue(priDois)
    assert len(xx) == 4
    assert xx.dequeue() == aia
    assert xx.search(0) == priDois
    assert xx.search(1) == baixo
    assert xx.search(2) == baixoDois
    with pytest.raises(IndexError):
        xx.search(3)
