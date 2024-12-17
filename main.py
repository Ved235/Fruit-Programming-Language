import sys
from fruit_lexer import FruitLexer
from fruit_parser import FruitParser
from fruit_interpreter import FruitInterpreter

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <file.fruit>")
        return

    file_path = sys.argv[1]
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    lexer = FruitLexer()
    parser = FruitParser()
    interpreter = FruitInterpreter()

    tokens = list(lexer.tokenize(code))
    ast = parser.parse(iter(tokens)) # Parse the tokens
    interpreter.run(ast) # Run the AST

if __name__ == "__main__":
    main()