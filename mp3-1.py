# Grammar
# <expr> ::= <expr>+<term> | <expr>-<term> | <term>
# <term> ::= <term>*<factor> | <term>/<factor> | <factor>
# <factor> ::= (<expr>) | <digit>
# <digit> ::= 0 | 1 | 2 | 3

# New Grammar
# <expr> ::= <term><E'>
# <E'> ::= +<term><E'> | -<term><E'> | ε
# <term> ::= <factor><F'>
# <F'> ::= *<factor><F'> | /<factor><F'> | ε
# <factor> ::= (<expr>) | <digit>
# <digit> ::= 0 | 1 | 2 | 3

import sys
digits = ['0', '1', '2', '3']
cursor = None

def parse():
    sys.stdout.write("\nInput: ")
    scan()
    if cursor == '$':
        sys.exit(1)
    expr()
    if cursor == '$':
        sys.stdout.write(", input is valid.")
    else:
        error(1)

def expr():
    term()
    while cursor == '+' or cursor == '-':
        scan()
        term()

def term():
    factor()
    while cursor == '*' or cursor == '/':
        scan()
        factor()

def factor():
    if cursor in digits: # if current letter is in the list
        scan()
    elif cursor == '(':
        scan()
        expr()
        if cursor == ')':
            scan()
        else:
            error(3)
    else:
        error(4)

def error(n):
    sys.stdout.write("\nError:" +
      str(n) + "\n")
    sys.exit(1)

def get_character():
    char = sys.stdin.read(1)
    if len(char) > 0:
        sys.stdout.write(char)
        return char
    else:
        return None

def scan():
    global cursor
    cursor = get_character()
    if cursor == None:
        sys.exit(1)
    while cursor.isspace(): # ignore whitespaces
        cursor = get_character()

while True:
    parse()