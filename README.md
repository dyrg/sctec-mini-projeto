# Mini-Projeto - Pré-processamento de Imagens com OpenCV

Pipeline em Python para pré-processar imagens de peças de fundição.

O objetivo não é classificar defeitos, e sim preparar as imagens para que um modelo de Machine Learning possa ser treinado posteriormente.

## Status

Em desenvolvimento.

## Estrutura

```
---
```

## Dataset

Baixar em: https://drive.google.com/file/d/1K5gNxQ7RXA-nb4boNzPYQTJlRvJyYBD1/view?usp=sharing

Copiar as imagens de `ok_front` e `def_front` para `raw_images/`.

## Como executar

Criar o ambiente virtual e instalar as dependências:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Executar o pipeline:

```bash
python main.py
```

O script lê as imagens de `raw_images/` em lote e grava o resultado em `processed_images/`.

## Licença

MIT
