import basicparser as b

data = '''
PRINT "HELLO WORLD"
PRINT 1245
PRINT 1234 + 678910
PRINT "vrot mnen nogi:", 2000
'''

dataIF = '''
FOR num = 10 TO 1 STEP -1
x = 100
PRINT x*1000
PRINT num*num
IF 100+200>20 THEN PRINT "HELLO WORD"
IF 222 = 2345 THEN PRINT "BLAH BLAH BLAH"
IF 234-234>234 THEN IF 555 = 0 THEN PRINT "nenene!"
NEXT num
'''

data4 = '''
num =100
x = 125
x = x*num
PRINT num
PRINT x
'''

data5 = '''
x
x = 1000 + 234
PRINT x
'''


INPUT = dataIF
print "input:\n%s\n"%INPUT
xxx = b.parse(INPUT)
print "parser out:\n%s"%xxx