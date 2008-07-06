from ply import *

keywords = (
    'IF','THEN','WHILE',
    'WEND','FOR','NEXT','PRINT','STEP','TO'
)

tokens = keywords + ('EQUALS','PLUS', 'TIMES','MINUS','DIVIDE','POWER',
     'LPAREN','RPAREN','LT','LE','GT','GE','NE',
     'COMMA','SEMI', 'INTEGER', 'STRING',
     'ID','NEWLINE')
     
t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    if t.value in keywords:
        t.type = t.value
    return t
    
t_EQUALS  = r'='
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_POWER   = r'\^'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LT      = r'<'
t_LE      = r'<='
t_GT      = r'>'
t_GE      = r'>='
t_NE      = r'<>'
t_COMMA   = r'\,'
t_SEMI    = r';'
t_INTEGER = r'\d+'    
#t_FLOAT   = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_STRING  = r'\".*?\"'

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t

def t_error(t):
    print "Illegal character", t.value[0]
    t.lexer.skip(1)

lex.lex()
