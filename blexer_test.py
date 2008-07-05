import basiclexer as lexer

data4 = '''
PRINT "HELLO WORLD"
'''
data = '''
FOR num = 5 TO 1 STEP -1
PRINT num + "*" + (num+1)
PRINT =
PRINT num*(num-1)
'''

dddd = [data,data4]
for elem in dddd:
    try:
        data = elem
        print "lexer test on string:\n%s "%data
        lexer.lex.input(data)
        while 1:            
            tok = lexer.lex.token()
            if not tok: break      # No more input
            print tok
    except EOFError:
        break