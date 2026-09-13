"""Ponto de entrada do pipeline de pré-processamento."""

from __future__ import annotations

import os
import sys
from collections import Counter

from src.loader import carregar_imagens, listar_imagens, salvar_imagem
from src.preprocess import preprocessar

DIRETORIO_ENTRADA = "raw_images"
DIRETORIO_SAIDA = "processed_images"


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
    processadas = 0

    for caminho_relativo, imagem in carregar_imagens(DIRETORIO_ENTRADA):
        resultado = preprocessar(imagem)
        salvar_imagem(resultado, DIRETORIO_SAIDA, caminho_relativo)

        classe = os.path.dirname(caminho_relativo) or "(raiz)"
        por_classe[classe] += 1
        processadas += 1

    print(f"Diretório de entrada: {DIRETORIO_ENTRADA}/")
    print(f"Diretório de saída: {DIRETORIO_SAIDA}/")
    print(f"Arquivos de imagem encontrados: {len(arquivos)}")
    print(f"Imagens processadas: {processadas}")
    print(f"Arquivos ignorados: {len(arquivos) - processadas}")
    print("Distribuição por classe:")

    for classe, total in sorted(por_classe.items()):
        print(f"  {classe}: {total}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
