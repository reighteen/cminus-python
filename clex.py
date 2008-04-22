#-*- coding:utf8 -*-
import sys
sys.path.insert(0,"../..")
import ply.lex as lex

 # Reserved words
reserved = (
    'INT','ELSE','VOID','IF','WHILE','RETURN','WRITE','READ',   
    )
tokens = reserved + (
    
    # Operators(=,+,-,*,/,<,>,<=,>=,==,!=)
    'ASSIGN','PLUS','MINUS','TIMES','DIV','LT','GT','NGT','NLT','EQ','NEQ',
    # Special characters((,),{,},[,],,,;,)
    'LPARAN','RPARAN','LBRACE','RBRACE','LSQUARE','RSQUARE','COMMA','SEMI',
    # Complex tokens
    'ID','NUM', 
    )

# Completely ignored whitepace,newline,comments
# Whitespace
def t_WHITESPACE(t):
    r'[ \t]+'
# Newlines
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
# Comments
def t_COMMENT(t):
    r' /\*(.|\n)*?\*/'
    t.lineno += t.value.count('\n')


# Operators
t_ASSIGN    = r'='
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIV       = r'/'
t_LT        = r'<'
t_GT        = r'>'
t_NGT       = r'<='
t_NLT       = r'>='
t_EQ        = r'=='
t_NEQ       = r'!='

# Special characters
t_LPARAN    = r'\('
t_RPARAN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_LSQUARE   = r'\['
t_RSQUARE   = r'\]'
t_COMMA     = r','
t_SEMI      = r';'

# Identifiers and reserved words
reserved_map = { }
for r in reserved:
    reserved_map[r.lower()] = r

def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value,"ID")
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# error handle
def t_error(t):
    print "Illegal character %s" % repr(t.value[0])
    t.lexer.skip(1)
    

#  ---------------------------------------------------------------
#  MAIN LEXER FUNCTIONALITY
#  ---------------------------------------------------------------

def run_lexer():
    """This is just a debugging function that prints out a list of
    tokens, it's not actually called by the compiler or anything."""
    if (len(sys.argv)==2):
      file = open(sys.argv[1])
      lines = file.readlines()
      file.close()
    else:
      print '''
            Usage: clex.py file   
            '''
      sys.exit(1)
    strings = ""
    for i in lines:
        strings += i
    lex.input(strings)
    while 1:
        token = lex.token()       # Get a token
        if not token: break        # No more tokens
        print "(%s,'%s',%d)" % (token.type, token.value, token.lineno)

lex.lex()

if __name__ == '__main__':
    run_lexer()

