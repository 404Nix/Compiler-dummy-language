import re

token_specification = [
    ('NUMBER',  r'\d+(\.\d*)?'),    # Integer or decimal number
    ('ID',      r'[A-Za-z_]\w*'),    # Identifier
    ('PLUS',    r'\+'),              # Plus operator
    ('MINUS',   r'-'),               # Minus operator
    ('TIMES',   r'\*'),              # Multiplication operator
    ('DIVIDE',  r'/'),               # Division operator
    ('ASSIGN',  r'='),               # Assignment operator
    ('PRINT',   r'print'),           # Print keyword
    ('SEMICOLON', r';'),             # Semicolon
    ('SKIP',    r'[ \t\n]'),         # Skip spaces, tabs, newlines
    ('OPEN_PAREN', r'\('),           # Open parenthesis
    ('CLOSE_PAREN', r'\)'),          # Close parenthesis
]

# Join the regular expressions into a single pattern
tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

def tokenize(code):
    tokens = []
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUMBER':
            value = int(value)  # Convert number string to integer
        elif kind == 'ID' and value in ('print',):
            kind = value.upper()  # Convert 'print' keyword to uppercase
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected')
        tokens.append((kind, value))
    return tokens

# Example usage
if __name__ == "__main__":
    code = "x = 10; y = 20; z = x + y; print(z);"
    tokens = tokenize(code)
    for token in tokens:
        print(token)
