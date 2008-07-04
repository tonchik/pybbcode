import bbcodeparser as b

data = '''

[u] mama mila ramu [/u] 


[url]http://bash.org.ru[/url]
'''
data2 = """MAMA
"""

#tags = (
#    'B_TAG','I_TAG','U_TAG','S_TAG','IMG_TAG','URL_TAG',
#    'QUOTE_TAG','CODE_TAG','SIZE_TAG','EMAIL_TAG', 'BASIC_TAG',
#    'B_TAG_CL','I_TAG_CL','U_TAG_CL','S_TAG_CL','IMG_TAG_CL','URL_TAG_CL',
#    'QUOTE_TAG_CL','CODE_TAG_CL','SIZE_TAG_CL','EMAIL_TAG_CL', 'BASIC_TAG_CL'
#)

data3 = '''[u]MAMA MILA RAMU[/u]
[u]BLAH[/u]
[url]http://bash.org.ru[/url]
sldjflsjf lsjdf lskd flsjdf [img]http://kartinka.ru/blah.jpg[/img] 
[quote] Quoted text[/quote]
[code] CODE [/code]
'''

INPUT = data3
print "input:\n%s\n"%INPUT
xxx = b.parse(INPUT)
print "parser out:\n%s"%xxx
