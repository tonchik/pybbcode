alpha ������ �������� ������.
���������� BBCode � html. ���� ������� ������ ����� ��� BASIC.
� �������� ����������� ������������ ���������� PLY(http://www.dabeaz.com/ply/)
�� python, ������� �������� � ���� ������ lex � yacc. ������� ���������� �������� � ������ �� �����������.
�� ��������� ���� ,��� �������� �� Python � ���������� ������ �� Python �� ��� ������ �������� ������� �����.

bbcodelexer.py - ��� lexer. ���������� token� � ����������� � ����������� �����������.  
lexer_test.py - ������ ����������� ��������������� ������ �������.
������ ������ lexer_test ����� � lexer_test.out

bbcodeparser.py parser. parser.out ���� ������ ������� ������������ �������������. 
��� ����� ������� ������� � ���������.

Grammar

Rule 1     statement -> statement expression
Rule 2     statement -> expression
Rule 3     expression -> IDW
Rule 4     expression -> expression IDW
Rule 5     expression -> ID
Rule 6     expression -> expression ID
Rule 7     expression -> B_TAG expression B_TAG_CL
Rule 8     expression -> S_TAG expression S_TAG_CL
Rule 9     expression -> U_TAG expression U_TAG_CL
Rule 10    expression -> I_TAG expression I_TAG_CL
Rule 11    expression -> IMG_TAG expression IMG_TAG_CL
Rule 12    expression -> URL_TAG expression URL_TAG_CL
Rule 13    expression -> QUOTE_TAG expression QUOTE_TAG_CL
Rule 14    expression -> CODE_TAG expression CODE_TAG_CL
Rule 15    expression -> SIZE_TAG expression SIZE_TAG_CL
Rule 16    expression -> NEWLINE

parser_test.py ����. ��������� ����� � parser_test.out

����� ����������� ��������� ���� basic �������������� � parser �������� ����������� ����������� ����� basic
� ����� �������� �������������, ������� ����� ��������� ����� ������� ���
check_loop, check_if � ���� ��������.

��������� ���� ���� ��������� ��������� ��� �� ������ ��������������, ����� ��������� �������� ���� basic.

[url]
[basic]
IF �����
    PRINT url1
ELSE
    PRINT url2
[/basic]
[/url]

�������� ����������� � ��� ������� ��� �� �����.

�� ���� ���������� ������� ��������� ����:

[basic]
    FOR i step 1
        [img]���������_i[/img]
[/basic]

� ������ ���������� �����,�����, ����������.