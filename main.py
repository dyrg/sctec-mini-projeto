"""Ponto de entrada da sprint 2: leitura em lote das imagens."""

from __future__ import annotations

import os
import sys
from collections import Counter

from src.loader import carregar_imagens, listar_imagens

DIRETORIO_ENTRADA = "raw_images"


def main() -> int:
    if not os.path.isdir(DIRETORIO_ENTRADA):
        print(f"[erro] diretório de entrada não encontrado: {DIRETORIO_ENTRADA}/")
        return 1

    arquivos = listar_imagens(DIRETORIO_ENTRADA)

    if not arquivos:
        print(f"[erro] nenhuma imagem encontrada em {DIRETORIO_ENTRADA}/")
        print("Baixe o dataset e copie as pastas 'def_front' e 'ok_front' para lá.")
        return 1

    por_classe: Counter[str] = Counter()
    carregadas = 0

    for caminho_relativo, _imagem in carregar_imagens(DIRETORIO_ENTRADA):
        classe = os.path.dirname(caminho_relativo) or "(raiz)"
        por_classe[classe] += 1
        carregadas += 1

    print(f"Diretório de entrada: {DIRETORIO_ENTRADA}/")
    print(f"Arquivos de imagem encontrados: {len(arquivos)}")
    print(f"Imagens carregadas: {carregadas}")
    print(f"Arquivos ignorados: {len(arquivos) - carregadas}")
    print("Distribuição por classe:")

    for classe, total in sorted(por_classe.items()):
        print(f"  {classe}: {total}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
