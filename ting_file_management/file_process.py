from ting_file_management.file_management import txt_importer
import sys


mensagem = "removido com sucesso"
mensagem2 = "Não há elementos"


def process(caminho, pensa):
    file_already_processed = any(
        item["nome_do_arquivo"] == caminho for item in pensa._files
    )
    if file_already_processed:
        return None
    xx = txt_importer(caminho)
    if xx is None:
        return None
    caminhoData = {
        "nome_do_arquivo": caminho,
        "qtd_linhas": len(xx),
        "linhas_do_arquivo": xx,
    }
    pensa.enqueue(caminhoData)
    print(caminhoData)


def remove(pensa):
    try:
        elimina = pensa.dequeue()
        if elimina:
            print(f"Arquivo {elimina['nome_do_arquivo']} {mensagem}")
        else:
            print(mensagem2)
    except IndexError:
        print(mensagem2)


def file_metadata(pensa, adição):
    """Aqui irá sua implementação"""
    try:
        item = pensa.search(adição)
        print(item)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
