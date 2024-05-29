class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.index = -1
        self.advance()

    def advance(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
        else:
            self.current_token = None

    def consume(self, expected_type):
        if self.current_token and self.current_token[0] == expected_type:
            self.advance()
        else:
            raise RuntimeError(f'Expected {expected_type} but got {self.current_token[0]}')

    def parse(self):
        program = ('PROGRAM', [])
        while self.current_token:
            if self.current_token[0] == 'ID':
                program[1].append(self.assignment())
            elif self.current_token[0] == 'PRINT':
                program[1].append(self.print_statement())
            else:
                raise RuntimeError(f'Unexpected token: {self.current_token[0]}')
        return program

    def assignment(self):
        var_name = self.current_token[1]
        self.consume('ID')
        self.consume('ASSIGN')
        value = self.expr()
        self.consume('SEMICOLON')
        return ('ASSIGN', (var_name, value))

    def print_statement(self):
        self.consume('PRINT')
        value = self.expr()
        self.consume('SEMICOLON')
        return ('PRINT', value)

    def expr(self):
        node = self.term()
        while self.current_token and self.current_token[0] in ('PLUS', 'MINUS'):
            token_type = self.current_token[0]
            self.advance()
            right = self.term()
            node = (token_type, node, right)
        return node

    def term(self):
        node = self.factor()
        while self.current_token and self.current_token[0] in ('TIMES', 'DIVIDE'):
            token_type = self.current_token[0]
            self.advance()
            right = self.factor()
            node = (token_type, node, right)
        return node

    def factor(self):
        token = self.current_token
        if token[0] == 'NUMBER':
            self.advance()
            return ('NUMBER', token[1])
        elif token[0] == 'ID':
            self.advance()
            return ('ID', token[1])
        elif token[0] == 'OPEN_PAREN':
            self.advance()
            node = self.expr()
            self.consume('CLOSE_PAREN')
            return node
        elif token[0] == 'MINUS':  # Handle unary minus
            self.advance()
            return ('UNARY_MINUS', self.factor())
        else:
            raise RuntimeError(f'Unexpected token: {token[0]}')
