from sly import Parser
from fruit_lexer import FruitLexer

class FruitParser(Parser):
    tokens = FruitLexer.tokens

    # Grammar rules and actions
    @_('statement_list')
    def program(self, p):
        return p.statement_list

    @_('statement_list statement')
    def statement_list(self, p):
        return p.statement_list + [p.statement]

    @_('statement')
    def statement_list(self, p):
        return [p.statement]

    @_('VARIABLE "=" expr')
    def statement(self, p):
        return ('assign', p.VARIABLE, p.expr)

    @_('expr MATH_OP expr')
    def expr(self, p):
        return (p.MATH_OP, p.expr0, p.expr1)

    @_('expr RELATIONAL_OP expr')
    def expr(self, p):
        return (p.RELATIONAL_OP, p.expr0, p.expr1)

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_('INT_OP expr')
    def expr(self, p):
        return ('int', p.expr)
        
    # Output (Squeeze)
    @_('OUTPUT expr')
    def statement(self, p):
        return ('print', p.expr)

    # Input (Pick)
    @_('INPUT VARIABLE')
    def statement(self, p):
        return ('input', p.VARIABLE)

    # Loop (Stir)
    @_('LOOP "(" expr ")" LBRACE statement_list RBRACE')
    def statement(self, p):
        return ('loop', p.expr, p.statement_list)

    # If-Else (TastesLike, Bitter)
    @_('IF "(" expr ")" LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE')
    def statement(self, p):
        return ('if_else', p.expr, p.statement_list0, p.statement_list1)

    @_('NUMBER')
    def expr(self, p):
        return ('num', p.NUMBER)

    @_('STRING')
    def expr(self, p):
        return ('str', p.STRING)

    @_('VARIABLE')
    def expr(self, p):
        return ('var', p.VARIABLE)

    # Error handling
    def error(self, p):
        if p:
            print(f"Syntax error at token {p.type} ('{p.value}')")
        else:
            print("Syntax error at EOF")

# Test Parser
if __name__ == "__main__":
    lexer = FruitLexer()
    parser = FruitParser()
    code = """
        Squeeze ("Hello World")
    """
    tokens = list(lexer.tokenize(code))
    print('Tokens:', tokens)
    result = parser.parse(iter(tokens))  # Convert list to iterator
    print('AST:', result)
