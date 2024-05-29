class CodeGenerator:
    def __init__(self):
        self.code = []
        self.temp_counter = 0

    def generate(self, node):
        if node[0] == 'PROGRAM':
            for statement in node[1]:
                self.generate(statement)
        elif node[0] == 'ASSIGN':
            var_name = node[1][0]
            value = self.generate(node[1][1])
            self.code.append(f'{var_name} = {value}')
        elif node[0] == 'PRINT':
            value = self.generate(node[1])
            self.code.append(f'print({value})')
        elif node[0] in ('PLUS', 'MINUS', 'TIMES', 'DIVIDE'):
            left = self.generate(node[1])
            right = self.generate(node[2])
            if node[0] == 'PLUS':
                temp = self.new_temp()
                self.code.append(f'{temp} = {left} + {right}')
                return temp
            elif node[0] == 'MINUS':
                temp = self.new_temp()
                self.code.append(f'{temp} = {left} - {right}')
                return temp
            elif node[0] == 'TIMES':
                temp = self.new_temp()
                self.code.append(f'{temp} = {left} * {right}')
                return temp
            elif node[0] == 'DIVIDE':
                temp = self.new_temp()
                self.code.append(f'{temp} = {left} / {right}')
                return temp
        elif node[0] == 'ID':
            return node[1]
        elif node[0] == 'NUMBER':
            return node[1]

    def new_temp(self):
        self.temp_counter += 1
        return f't{self.temp_counter}'
