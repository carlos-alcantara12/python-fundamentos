# Python Fundamentals

This repository documents my early foundation in **Python** through lessons, selected exercises, and small practice applications.

Its purpose is to record concepts I have already studied while developing programming logic, input validation, code readability, and basic organization.

## Repository Scope

This is a **fundamentals repository**, not a collection of standalone portfolio projects. Larger applications will receive their own repositories when they have independent requirements, structure, documentation, and development history.

## Structure

```text
python-fundamentos/
├── aulas/        # sequence of concepts studied
├── exercicios/   # focused practice of programming fundamentals
└── projetos/     # small applications built during the learning process
```

> The directory names remain in Portuguese because they reflect the original organization of my studies.

## Small Practice Applications

### Web Calculator

A Streamlit application used to practice functions, numeric input validation, exception handling, and a simple web interface.

File: [`projetos/calculadora_web.py`](./projetos/calculadora_web.py)

### Terminal Calculator

A command-line calculator with numeric input validation, supported-operator checks, and division-by-zero handling.

File: [`projetos/calculadora_terminal.py`](./projetos/calculadora_terminal.py)

### Secret Word Game

A terminal exercise used to practice loops, strings, sets, input validation, and control flow.

File: [`projetos/palavra_secreta.py`](./projetos/palavra_secreta.py)

## Fundamentals Practiced

- data types and variables;
- arithmetic and logical operators;
- conditional statements;
- `for` and `while` loops;
- strings;
- lists, tuples, and sets;
- unpacking and `enumerate`;
- basic functions;
- exception handling;
- input validation.

## Running the Applications

Clone the repository:

```bash
git clone https://github.com/carlos-alcantara12/python-fundamentos.git
cd python-fundamentos
```

Run a terminal application, for example:

```bash
python projetos/calculadora_terminal.py
```

To run the web calculator:

```bash
pip install -r requirements.txt
streamlit run projetos/calculadora_web.py
```

## Current Stage

The code reflects an early stage of my programming education. I am keeping this repository focused on concepts I can explain and develop at my current level.
