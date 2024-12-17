class FruitInterpreter:
    def __init__(self):
        self.env = {}

    def evaluate(self, node):
        if isinstance(node, tuple):
            if node[0] == 'assign':
                self.env[node[1]] = self.evaluate(node[2])
            elif node[0] == 'print':
                print(self.evaluate(node[1]))
            elif node[0] == 'input':
                self.env[node[1]] = input()
            elif node[0] == 'Mash':
                left = self.evaluate(node[1])
                right = self.evaluate(node[2])
                if isinstance(left, str) or isinstance(right, str):
                    return str(left) + str(right)
                return left + right
            elif node[0] == 'Peel':
                return self.evaluate(node[1]) - self.evaluate(node[2])
            elif node[0] == 'Grow':
                return self.evaluate(node[1]) * self.evaluate(node[2])  # Multiply
            elif node[0] == 'Slice':
                return self.evaluate(node[1]) / self.evaluate(node[2])  # Divide
            elif node[0] == 'RiperThan':
                return self.evaluate(node[1]) > self.evaluate(node[2])  # Greater than
            elif node[0] == 'LessFresh':
                return self.evaluate(node[1]) < self.evaluate(node[2])  # Less than
            elif node[0] == 'int':
                return int(self.evaluate(node[1]))  # Integer conversion
            elif node[0] == 'loop':
                while self.evaluate(node[1]):
                    for stmt in node[2]:
                        self.evaluate(stmt)
            elif node[0] == 'if_else':
                if self.evaluate(node[1]):
                    for stmt in node[2]:
                        self.evaluate(stmt)
                else:
                    for stmt in node[3]:
                        self.evaluate(stmt)
            elif node[0] == 'num':
                return int(node[1])
            elif node[0] == 'str':
                return node[1]
            elif node[0] == 'var':
                var_name = node[1]
                if var_name in self.env:
                    return self.env[var_name]
                else:
                    raise ValueError(f"Undefined variable: {var_name}")
        else:
            raise ValueError(f"Unknown node type: {node}")

    def run(self, ast):
        for node in ast:
            self.evaluate(node)

# Test Interpreter
if __name__ == "__main__":
    from fruit_parser import FruitParser
    from fruit_lexer import FruitLexer

    code = """
        Squeeze ("Hello World")
    """
    lexer = FruitLexer()
    parser = FruitParser()
    interpreter = FruitInterpreter()

    tokens = list(lexer.tokenize(code))
    print('Tokens:', tokens)
    ast = parser.parse(iter(tokens))
    print('AST:', ast)
    interpreter.run(ast)