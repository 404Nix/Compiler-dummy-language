# Dummy Language to Python Compiler

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-Completed-brightgreen.svg)

## Introduction
This project implements a simple compiler that translates a custom Dummy language into Python code. It demonstrates the phases of compiler design: Lexical Analysis, Syntax Analysis, Semantic Analysis, Intermediate Code Generation, and Final Code Generation. The compiler reads Dummy language code, tokenizes it, parses it into an Abstract Syntax Tree (AST), checks for semantic correctness, and generates executable Python code. This project serves as a practical example of compiler design principles, showcasing the translation from a high-level custom language to another high-level language.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Example](#example)
- [Requirements](#requirements)
- [Limitations](#limitations)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Features
- **Lexical Analysis**: Tokenizes Dummy language code.
- **Syntax Analysis**: Produces an Abstract Syntax Tree (AST).
- **Semantic Analysis**: Ensures semantic correctness.
- **Code Generation**: Generates executable Python code.

## Project Structure
.
├── compiler.py # Main driver script
├── tokenizer.py # Lexical analyzer
├── parser.py # Syntax analyzer
├── semantic_analyzer.py # Semantic analyzer
├── code_generator.py # Code generator
├── source_code.txt # Sample Dummy language code
└── README.md # Project documentation

## Usage
1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/dummy-language-compiler.git
    cd dummy-language-compiler
    ```

2. **Prepare your Dummy language source code** in `source_code.txt`.

3. **Run the compiler**:
    ```bash
    python compiler.py -f source_code.txt
    ```

4. **Generated Python code** will be saved in `output_code.py`.

## Example
### Input (Dummy Language Code)
x = 10;
y = 20;
z = x + y;
print(z);


### Output (Generated Python Code)
```python
x = 10
y = 20
z = x + y
print(z)

Requirements
Python 3.x
Limitations
Only supports basic arithmetic operations and print statements.
No support for complex data types or control structures.
Future Enhancements
Add support for more complex language constructs.
Implement optimizations for the generated code.
Improve error handling and reporting.
License
This project is licensed under the MIT License. See the LICENSE file for details.

