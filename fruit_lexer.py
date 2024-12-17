from sly import Lexer

class FruitLexer(Lexer):
    # Token definitions
    tokens = { 
        VARIABLE, NUMBER, STRING, RELATIONAL_OP, MATH_OP, INPUT, OUTPUT, LBRACE, RBRACE, INT_OP, LOOP, IF, ELSE
    }
    literals = { '=', ':', ',', '(', ')' }  # Used directly in the language
    ignore = ' \t'  # Ignore spaces and tabs

    LBRACE = r'\{'
    RBRACE = r'\}'

    # Relational operators
    RELATIONAL_OP = r'RiperThan|LessFresh|Equals'

    # Math operators
    MATH_OP = r'Mash|Peel|Grow|Slice'

    # Integer conversion operator
    INT_OP = r'🍈'

    # Input/Output actions
    @_(r'Pick')
    def INPUT(self, t):
        return t
    
    @_(r'Squeeze')
    def OUTPUT(self, t):
        return t
    
    @_(r'Stir')
    def LOOP(self, t):
        return t
    
    @_(r'TastesLike')
    def IF(self, t):
        return t   
    
    @_(r'Bitter')
    def ELSE(self, t):
        return t

    # Numbers (integer or float)
    @_(r'-?\d+(\.\d+)?')
    def NUMBER(self, t):
        t.value = float(t.value) if '.' in t.value else int(t.value)
        return t

    # Strings (for output or variable values)
    @_(r'\".*?\"')
    def STRING(self, t):
        t.value = t.value[1:-1]  # Remove surrounding quotes
        return t

    # Variable names (must start with 🍎 and followed by letters, digits, or underscores)
    @_(r'🍎[a-zA-Z_][a-zA-Z0-9_]*')
    def VARIABLE(self, t):
        return t

    # Newlines (to track line numbers)
    @_(r'\n+')
    def newline(self, t):
        self.lineno += len(t.value)

    # Comments (start with //)
    @_(r'//.*')
    def COMMENT(self, t):
        pass

    @_(r'\s+')
    def ignore_whitespace(self, t):
        pass

    # Track line numbers for error reporting
    def error(self, t):
        print(f"Illegal character {t.value[0]} at line {self.lineno}")
        self.index += 1


# Test Lexer
if __name__ == "__main__":
    lexer = FruitLexer()
    code = """
        Squeeze ("Hello World")
    """
    for token in lexer.tokenize(code):
        print(token)
