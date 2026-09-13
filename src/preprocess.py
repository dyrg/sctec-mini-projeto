"""Funções de pré-processamento das imagens."""

from __future__ import annotations

import cv2
import numpy as np

KERNEL_BLUR = 5


def converter_para_cinza(imagem: np.ndarray) -> np.ndarray:
    """Converte a imagem de BGR para escala de cinza."""
    return cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)


def suavizar(imagem: np.ndarray, kernel: int = KERNEL_BLUR) -> np.ndarray:
    """Aplica Gaussian Blur para reduzir o ruído da imagem."""
    return cv2.GaussianBlur(imagem, (kernel, kernel), 0)


def preprocessar(imagem: np.ndarray) -> np.ndarray:
    """Aplica as etapas básicas de pré-processamento."""
    cinza = converter_para_cinza(imagem)
    return suavizar(cinza)
