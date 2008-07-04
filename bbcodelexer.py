from ply import *
import re

src_tags = ('b','i','u','s','img','url','quote','code','size','email', 'basic')

tags = (
    'B_TAG','I_TAG','U_TAG','S_TAG','IMG_TAG','URL_TAG',
    'QUOTE_TAG','CODE_TAG','SIZE_TAG','EMAIL_TAG', 'BASIC_TAG',
    'B_TAG_CL','I_TAG_CL','U_TAG_CL','S_TAG_CL','IMG_TAG_CL','URL_TAG_CL',
    'QUOTE_TAG_CL','CODE_TAG_CL','SIZE_TAG_CL','EMAIL_TAG_CL', 'BASIC_TAG_CL'
)

keywords = (
    'IF','THEN','ELSEIF','END','WHILE',
    'WEND','FOR','NEXT'
)

tokens = keywords + tags + (
     'EQUALS','PLUS', 'TIMES','MINUS','DIVIDE','POWER',
     'LPAREN','RPAREN','LT','LE','GT','GE','NE',
     'COMMA','SEMI', 'INTEGER','FLOAT', 'STRING',
     'ID','IDW','NEWLINE'
)

t_ignore = ' \t'


#tags
def t_TAG(t):
    r'\[[/\w]*\]'
    cur_tag = re.sub('[\[\]]',"",t.value)

    if cur_tag[0] == '/' and cur_tag[1:] in src_tags:
        t.type = cur_tag[1:].upper() + '_TAG_CL'
        t.value = cur_tag[1:]
        return t
    elif cur_tag in src_tags:
        t.type = cur_tag.upper() + '_TAG'
        t.value = cur_tag
        return t
def t_SIZE_TAG(t):
    r'\[size=[\d]*\]'
    t.value = re.search(r'(?<=\[size=)[\d]*(?=\])',t.value).group()
    return t
    
#simple tokens
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
t_FLOAT   = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_STRING  = r'\".*?\"'

def t_IDW(t):
    r'[a-zA-Z0-9_:/.]+'
    
    pat = re.compile('[a-zA-Z][a-zA-Z0-9_]*')
    res = pat.match(t.value)
    
    
    if res and res.group() == t.value:
        t.type = 'ID'     
    if t.value in keywords:
        t.type = t.value
    return t

def t_INTEGER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print "Integer value too large", t.value
        t.value = 0
    #print "parsed number %s" % repr(t.value)
    return t

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t

def t_error(t):
    print "Illegal character", t.value[0]
    t.lexer.skip(1)

lex.lex()