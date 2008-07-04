from ply import *
import bbcodelexer
import re
tokens = bbcodelexer.tokens

def p_s_e(p):
    ''' statement : statement expression
        | expression
    '''
    if len(p) == 3:
        p[0] = p[1] + " " + p[2]
    elif len(p) == 2:
        p[0] = p[1]
def p_expression_IDW(p):
    '''expression : IDW
        | expression IDW
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1] + " " + p[2]

def p_expression_ID(p):
    '''expression : ID
        | expression ID
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1] + " " + p[2]
    #print p[0]
    
#def p_statement_expression(p):
    #'''statement : expression '''
    #print p[1]

#def p_statement_expr(p):
        #'''statement : I_TAG '''
        #p[0] = "BLAH"


#tags = (
#    'B_TAG','I_TAG','U_TAG','S_TAG','IMG_TAG','URL_TAG',
#    'QUOTE_TAG','CODE_TAG','SIZE_TAG','EMAIL_TAG', 'BASIC_TAG',
#    'B_TAG_CL','I_TAG_CL','U_TAG_CL','S_TAG_CL','IMG_TAG_CL','URL_TAG_CL',
#    'QUOTE_TAG_CL','CODE_TAG_CL','SIZE_TAG_CL','EMAIL_TAG_CL', 'BASIC_TAG_CL'
#)
        
def p_tag_expression(p):
    '''expression : B_TAG expression B_TAG_CL
                  | S_TAG expression S_TAG_CL
                  | U_TAG expression U_TAG_CL
                  | I_TAG expression I_TAG_CL
                  | IMG_TAG expression IMG_TAG_CL
                  | URL_TAG expression URL_TAG_CL
                  | QUOTE_TAG expression QUOTE_TAG_CL
                  | CODE_TAG expression CODE_TAG_CL
                  '''
    cur_tag = p[1]
    if cur_tag in ['i','s','b','u']:
        p[0] = "<%s>%s</%s>"%(cur_tag,p[2],cur_tag)
    elif cur_tag == 'img':
        p[0] = "<%s src=%s>"%(cur_tag,p[2])
    elif cur_tag == 'url':
        p[0] = "<a href=%s>%s</a>"%(p[2],p[2])
    elif cur_tag == 'quote':
        p[0] = "<blockquote><p>%s</p></blockquote>"%(p[2])
    elif cur_tag == 'code':
        p[0] = "<pre>%s</pre>"%(p[2])

def p_sizetag_expression(p):
    ''' expression : SIZE_TAG expression SIZE_TAG_CL'''
    p[0] = '<span style\"font-size:%dpx\">%s</span>'%(p[1],p[2])
    
#ignore new lines
def p_statement_newline(p):
    '''expression : NEWLINE'''
    p[0] = ''
    
#### Catastrophic error handler
def p_error(p):
    if not p:
        print "SYNTAX ERROR AT EOF"

bbcodeparser = yacc.yacc()

def parse(data):
    bbcodeparser.error = 0
    p = bbcodeparser.parse(data)
    if bbcodeparser.error: return None
    return p