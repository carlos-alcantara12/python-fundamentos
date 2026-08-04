# Python Fundamentos

Repositório de estudos de Python básico: tipos de dados, operadores, condicionais,
laços de repetição (`for`/`while`), listas, tuplas, desempacotamento, strings e
manipulação de arquivos de exercícios práticos.

## Estrutura

- `aula*.py` — exercícios e demonstrações de conceitos individuais, em ordem de estudo.
- `exer*.py` / `exercicio_*.py` — exercícios práticos aplicando os conceitos.
- `palavrasecreta.py` — jogo de forca simplificado (loop, validação de entrada, strings).
- `calculadora2.py` — calculadora de terminal com validação de entrada via `try/except`.
- `testebase.py` — exercício de manipulação de strings (indexação, slicing).
- `app.py` — calculadora com interface web, feita com [Streamlit](https://streamlit.io).

## Como rodar

A maioria dos arquivos é independente e pode ser executada diretamente:

```bash
python aula1.py
```

O `app.py` depende do Streamlit. Para rodá-lo:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Status

Material de estudo em progresso — parte do aprendizado de Python básico antes de
avançar para tópicos intermediários (dicionários, funções, módulos, programação
funcional).
