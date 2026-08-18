# Python Fundamentos

Repositório que registra minha base em **Python** por meio de aulas, exercícios e pequenos projetos.

O foco aqui é documentar a evolução nos fundamentos da linguagem com atenção a **lógica de programação, validação de dados, legibilidade e organização de código**.

## Estrutura

```text
python-fundamentos/
├── aulas/        # sequência dos conceitos estudados
├── exercicios/   # prática isolada dos fundamentos
└── projetos/     # aplicações completas construídas durante o estudo
```

## Projetos em destaque

### Calculadora Web
Aplicação com **Streamlit**, validação de entrada, tratamento de erros e separação entre lógica de cálculo e interface.

Arquivo: [`projetos/calculadora_web.py`](./projetos/calculadora_web.py)

### Calculadora de Terminal
Calculadora de linha de comando com validação numérica, operadores permitidos e proteção contra divisão por zero.

Arquivo: [`projetos/calculadora_terminal.py`](./projetos/calculadora_terminal.py)

### Palavra Secreta
Jogo em terminal para praticar laços, strings, coleções, validação de entrada e controle de fluxo.

Arquivo: [`projetos/palavra_secreta.py`](./projetos/palavra_secreta.py)

## Fundamentos praticados

- tipos de dados e variáveis;
- operadores aritméticos e lógicos;
- condicionais;
- laços `for` e `while`;
- strings;
- listas e tuplas;
- desempacotamento;
- `enumerate`;
- funções;
- tratamento de exceções;
- validação de dados.

## Executando

Clone o repositório:

```bash
git clone https://github.com/carlos-alcantara12/python-fundamentos.git
cd python-fundamentos
```

Exemplo de projeto de terminal:

```bash
python projetos/calculadora_terminal.py
```

Para a calculadora web:

```bash
pip install -r requirements.txt
streamlit run projetos/calculadora_web.py
```

## Sobre

Este repositório representa uma etapa inicial da minha formação em programação e serve como registro técnico dos fundamentos que sustentam meus estudos em Engenharia da Computação e Segurança da Informação.
