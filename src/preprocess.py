"""Funções de pré-processamento das imagens."""

from __future__ import annotations

import cv2
import numpy as np

KERNEL_BLUR = 5
KERNEL_MORFOLOGIA = 3
LIMIAR_CANNY_BAIXO = 50
LIMIAR_CANNY_ALTO = 150
TAMANHO_PADRAO = (256, 256)


def converter_para_cinza(imagem: np.ndarray) -> np.ndarray:
    """Converte a imagem de BGR para escala de cinza."""
    return cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)


def suavizar(imagem: np.ndarray, kernel: int = KERNEL_BLUR) -> np.ndarray:
    """Aplica Gaussian Blur para reduzir o ruído da imagem."""
    return cv2.GaussianBlur(imagem, (kernel, kernel), 0)


def limiarizar(imagem: np.ndarray) -> np.ndarray:
    """Aplica limiarização com Otsu."""
    _, resultado = cv2.threshold(imagem, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return resultado


def detectar_bordas(imagem: np.ndarray) -> np.ndarray:
    """Detecta bordas com Canny."""
    return cv2.Canny(imagem, LIMIAR_CANNY_BAIXO, LIMIAR_CANNY_ALTO)


def refinar_mascara(imagem: np.ndarray, kernel: int = KERNEL_MORFOLOGIA) -> np.ndarray:
    """Remove pequenos ruídos com abertura morfológica."""
    elemento = np.ones((kernel, kernel), np.uint8)
    return cv2.morphologyEx(imagem, cv2.MORPH_OPEN, elemento)


def redimensionar(imagem: np.ndarray, tamanho: tuple[int, int] = TAMANHO_PADRAO) -> np.ndarray:
    """Redimensiona a imagem para o tamanho padrão."""
    return cv2.resize(imagem, tamanho)


def preprocessar(imagem: np.ndarray) -> np.ndarray:
    """Aplica o pipeline completo de pré-processamento."""
    cinza = converter_para_cinza(imagem)
    suave = suavizar(cinza)
    mascara = limiarizar(suave)
    refinada = refinar_mascara(mascara)
    bordas = detectar_bordas(refinada)
    return redimensionar(bordas)
