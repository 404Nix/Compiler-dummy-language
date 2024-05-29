class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}

    def analyze(self, node):
        if node[0] == 'PROGRAM':
            for statement in node[1]:
                self.analyze(statement)
        elif node[0] == 'ASSIGN':
            var_name = node[1][0]
            value = self.analyze(node[1][1])
            self.symbol_table[var_name] = value
        elif node[0] == 'PRINT':
            value = self.analyze(node[1])
            print(value)  # Assuming you want to print the value during semantic analysis
        elif node[0] in ('PLUS', 'MINUS', 'TIMES', 'DIVIDE'):
            left = self.analyze(node[1])
            right = self.analyze(node[2])
            if node[0] == 'PLUS':
                return left + right
            elif node[0] == 'MINUS':
                return left - right
            elif node[0] == 'TIMES':
                return left * right
            elif node[0] == 'DIVIDE':
                return left / right
        elif node[0] == 'ID':
            return self.symbol_table.get(node[1])
        elif node[0] == 'NUMBER':
            return node[1]
        else:
            raise RuntimeError(f'Invalid node: {node[0]}')

# Example usage
if __name__ == "__main__":
    from my_parser import Parser
    from tokenizer import tokenize

    code = "x = 10; y = 20; z = x + y; print(z);"
    tokens = tokenize(code)
    parser = Parser(tokens)
    ast = parser.parse()
    semantic_analyzer = SemanticAnalyzer()
    semantic_analyzer.analyze(ast)
