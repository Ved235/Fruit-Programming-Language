# 🍎 Fruit Programming Language

A simple programming language that uses fruit-themed keywords and emoji variables. Written in Python using SLY for lexing and parsing.

## Installation

```bash
pip install sly
git clone <repository-url>
cd fruit-programming-language
```

## Usage

Run a Fruit program:
```bash
python main.py <filename.fruit>
```

## Syntax Guide

### Variables
- Variables must start with 🍎 followed by letters, numbers, or underscores
```fruit
🍎age = 25
🍎name = "Apple"
```

### Output
- Use `Squeeze` to print values
```fruit
Squeeze ("Hello World")
Squeeze 🍎age
```

### Input 
- Use `Pick` to get user input
```fruit
Pick 🍎userInput
```

### Mathematical Operations
- `Mash`: Addition (+)
- `Peel`: Subtraction (-)
- `Grow`: Multiplication (*)
- `Slice`: Division (/)

```fruit
🍎result = (🍎a Mash 🍎b)
🍎difference = (🍎x Peel 🍎y)
```

### Relational Operators
- `RiperThan`: Greater than (>)
- `LessFresh`: Less than (<)
- `Equals`: Equal to (=)

### Control Flow

#### If-Else Statements
```fruit
TastesLike (🍎age RiperThan 18) {
    Squeeze ("You are an adult")
} Bitter {
    Squeeze ("You are a minor")
}
```

#### Loops
```fruit
🍎i = 0
Stir (🍎i LessFresh 5) {
    Squeeze 🍎i
    🍎i = (🍎i Mash 1)
}
```

### Examples

1. Hello World:
```fruit
Squeeze ("Hello World")
```

2. Basic Calculator:
```fruit
🍎a = 5
🍎b = 3
🍎sum = (🍎a Mash 🍎b)
Squeeze 🍎sum
```

3. Fibonacci Sequence:
```fruit
🍎n = 10
🍎a = 0
🍎b = 1
🍎i = 2
Squeeze 🍎a
Squeeze 🍎b
Stir (🍎i LessFresh 🍎n) {
    🍎c = (🍎a Mash 🍎b)
    Squeeze 🍎c
    🍎a = 🍎b
    🍎b = 🍎c
    🍎i = (🍎i Mash 1)
}
```

## Technical Details

The implementation consists of three main components:
- 

- fruit_lexer.py - Tokenizes the source code


- fruit_parser.py - Parses tokens into an Abstract Syntax Tree


- fruit_interpreter.py - Executes the parsed AST
