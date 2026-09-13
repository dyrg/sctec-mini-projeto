"""Funções para encontrar e carregar imagens do dataset."""

from __future__ import annotations

import glob
import os
from collections.abc import Iterator

import cv2
import numpy as np

EXTENSOES_SUPORTADAS = (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff")


def listar_imagens(
    diretorio: str,
    extensoes: tuple[str, ...] = EXTENSOES_SUPORTADAS,
) -> list[str]:
    """Lista imagens nas subpastas de classe, sempre na mesma ordem."""
    padrao = os.path.join(diretorio, "**", "*")
    arquivos = [
        caminho
        for caminho in glob.glob(padrao, recursive=True)
        if os.path.isfile(caminho) and caminho.lower().endswith(extensoes)
    ]
    return sorted(arquivos)


def carregar_imagens(
    diretorio: str,
    extensoes: tuple[str, ...] = EXTENSOES_SUPORTADAS,
) -> Iterator[tuple[str, np.ndarray]]:
    """Carrega uma imagem por vez e mantém a classe no caminho relativo."""
    # Usando gerador para evitar carregar o dataset inteiro na memória
    for caminho in listar_imagens(diretorio, extensoes):
        imagem = cv2.imread(caminho)

        if imagem is None:
            print(f"[aviso] arquivo ignorado (não foi possível decodificar): {caminho}")
            continue

        yield os.path.relpath(caminho, diretorio), imagem
