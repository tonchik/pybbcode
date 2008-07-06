from ply import *
import basiclexer

tokens = basiclexer.tokens

precedence = (
               ('left', 'PLUS','MINUS'),
               ('left', 'TIMES','DIVIDE'),
               ('left', 'POWER'),
               ('right','UMINUS')
)

def p_program(p):
    '''program : program statement
               | statement'''
    if len(p)==2 and p[1]:
        p[0] = []
        p[0].append(p[1])
    elif len(p)==3:
        p[0] = p[1]
        if not p[0]:
            p[0] = []
        if p[2]:
            p[0].append(p[2])


def p_statement(p):
    '''statement : command NEWLINE'''
    p[0] = p[1]

#### Blank line

def p_statement_newline(p):
    '''statement : NEWLINE'''
    p[0] = None

def p_command_decl(p):
    '''command : variable EQUALS expr
                | variable
                '''
    val = None
    if len(p)==4:
        val = p[3]
        
    p[0] = ('DECL',p[1],val)
    
def p_command_print(p):
    '''command : PRINT plist'''
    p[0] = ('PRINT',p[2])

def p_expr_binary(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr
            | expr POWER expr'''

    p[0] = ('BINOP',p[2],p[1],p[3])

def p_expr_number(p):
    '''expr : INTEGER
    '''
    p[0] = ('NUM',eval(p[1]))

def p_expr_variable(p):
    '''expr : variable'''
    p[0] = ('VAR',p[1])

def p_expr_group(p):
    '''expr : LPAREN expr RPAREN'''
    p[0] = ('GROUP',p[2])

def p_expr_unary(p):
    '''expr : MINUS expr %prec UMINUS'''
    p[0] = ('UNARY','-',p[2])

def p_plist(p):
    '''plist   : plist COMMA pitem
               | pitem'''
    if len(p) > 3:
       p[0] = p[1]
       p[0].append(p[3])
    else:
       p[0] = [p[1]]

def p_item_string(p):
    '''pitem : STRING'''
    p[0] = (p[1][1:-1],None)

def p_item_string_expr(p):
    '''pitem : STRING expr'''
    p[0] = (p[1][1:-1],p[2])

def p_item_expr(p):
    '''pitem : expr'''
    p[0] = ("",p[1])

#if
def p_command_if(p):
    '''command : IF relexpr THEN command'''
    p[0] = ('IF',p[2],p[4])

# rel expression
def p_relexpr(p):
    '''relexpr : expr LT expr
               | expr LE expr
               | expr GT expr
               | expr GE expr
               | expr EQUALS expr
               | expr NE expr'''
    p[0] = ('RELOP',p[2],p[1],p[3])

#FOR

def p_command_for(p):
    '''command : FOR ID EQUALS expr TO expr optstep'''
    p[0] = ('FOR',p[2],p[4],p[6],p[7])

#Optional STEP qualifier on FOR statement

def p_optstep(p):
    '''optstep : STEP expr
               | empty'''
    if len(p) == 3:
       p[0] = p[2]
    else:
       p[0] = None

def p_command_next(p):
    '''command : NEXT ID'''

    p[0] = ('NEXT',p[2])

#### Variables
def p_variable(p):
    '''variable : ID
              | ID LPAREN expr RPAREN
              | ID LPAREN expr COMMA expr RPAREN'''
    if len(p) == 2:
       p[0] = (p[1],None,None)
    elif len(p) == 5:
       p[0] = (p[1],p[3],None)
    else:
       p[0] = (p[1],p[3],p[5])

### Builds a list of variable targets as a Python list

# def p_varlist(p):
    # '''varlist : varlist COMMA variable
               # | variable'''
    # if len(p) > 2:
       # p[0] = p[1]
       # p[0].append(p[3])
    # else:
       # p[0] = [p[1]]
       
#### Empty

def p_empty(p):
    '''empty : '''

#### Catastrophic error handler
def p_error(p):
    if not p:
        print "SYNTAX ERROR AT EOF"

bparser = yacc.yacc()

def parse(data):
    bparser.error = 0
    p = bparser.parse(data)
    if bparser.error: return None
    return p