import bbcodelexer as lexer
data = '''[i] mama mila ramu [/i] [img]http://blahblahblah.ru[/img]'''
data2 = ''''''    
data3 = """[size=15]big text[/size]
"""

data4 = '''[u]MAMA MILA RAMU[/u]
[u]BLAH[/u]
[url]http://bash.org.ru[/url]
sldjflsjf lsjdf lskd flsjdf [img]http://kartinka.ru/blah.jpg[/img] 
[quote] Quoted text[/quote]
[code] CODE [/code]
'''

dddd = [data,data2,data3,data4]
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