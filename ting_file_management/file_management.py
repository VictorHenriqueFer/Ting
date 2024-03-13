import sys
import os


def txt_importer(caminho):
    if not caminho.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")
        return None
    if not os.path.exists(caminho):
        sys.stderr.write(f"Arquivo {caminho} não encontrado\n")
        return None
    with open(caminho, "r") as file:
        return file.read().split("\n")
