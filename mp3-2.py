# Grammar
# <expr> ::= +<num> | -<num> | <num>
# <num> ::= <digits> | <digits>.<digits>
# <digits> ::= <digits><digit> | <digit>
# <digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

# New Grammar
# <expr> ::= <expr1> | <expr2> | <num>
# <expr1> ::= +<num>
# <expr2> ::= -<num>
# <num> ::= <digits><N>
# <N> ::= .<digits> | ε 
# <digits> ::= <digit><E'>
# <E'> ::= <digit><E'> | ε
# <digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

import sys
digits_arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
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
    expr1()
    expr2()
    num()

def expr1():
	if (cursor == '+'):
		scan()
		num()

def expr2():
	if (cursor == '-'):
		scan()
		num()

def num():
    digits()
    if (cursor == '.'):
        scan()
        digits()
        if (cursor == '.'):
        	error(2)

def digits():
    while cursor in digits_arr: # if current letter is in the list
        scan()

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