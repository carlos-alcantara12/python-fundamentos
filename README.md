# Python Fundamentals

This repository documents my foundation in **Python** through lessons, exercises, and small projects.

The goal is to record my progress with the language while developing **programming logic, data validation, code readability, and code organization**.

## Structure

```text
python-fundamentos/
├── aulas/        # sequence of concepts studied
├── exercicios/   # focused practice of programming fundamentals
└── projetos/     # small applications built during the learning process
```

> The directory names remain in Portuguese because they reflect the original organization of my studies.

## Featured Projects

### Web Calculator
A **Streamlit** application with input validation, error handling, and separation between calculation logic and the user interface.

File: [`projetos/calculadora_web.py`](./projetos/calculadora_web.py)

### Terminal Calculator
A command-line calculator with numeric input validation, supported-operator checks, and division-by-zero protection.

File: [`projetos/calculadora_terminal.py`](./projetos/calculadora_terminal.py)

### Secret Word Game
A terminal game created to practice loops, strings, collections, input validation, and control flow.

File: [`projetos/palavra_secreta.py`](./projetos/palavra_secreta.py)

## Fundamentals Practiced

- data types and variables;
- arithmetic and logical operators;
- conditional statements;
- `for` and `while` loops;
- strings;
- lists and tuples;
- unpacking;
- `enumerate`;
- functions;
- exception handling;
- data validation.

## Running the Projects

Clone the repository:

```bash
git clone https://github.com/carlos-alcantara12/python-fundamentos.git
cd python-fundamentos
```

Run a terminal project, for example:

```bash
python projetos/calculadora_terminal.py
```

To run the web calculator:

```bash
pip install -r requirements.txt
streamlit run projetos/calculadora_web.py
```

## About This Repository

This repository represents an early stage of my programming education and serves as a technical record of the fundamentals supporting my studies in Computer Engineering and my growing interest in cybersecurity.
