alpha версия курсовой работы.
Транслятор BBCode в html. Пока сделана только часть без BASIC.
В качестве инструмента используется библиотека PLY(http://www.dabeaz.com/ply/)
на python, которая включает в себя модули lex и yacc. Которые аналогичны утилитам с такими же названиеями.
Но благодаря тому ,что написаны на Python и генерируют парсер на Python на мой взгляд работать намного проще.

bbcodelexer.py - это lexer. Генерирует tokenы в соответсвии с регулярными выражениями.  
lexer_test.py - скрипт позволяющий визуализировать рабуту лексера.
Пример работы lexer_test лежит в lexer_test.out

bbcodeparser.py parser. parser.out файл дебага который генерируется автоматически. 
Там можно увидеть таблицу и состояния.

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

parser_test.py тест. Результат теста в parser_test.out

Чтобы реализовать поддержку тэга basic предполагается в parser заносить управляющие конструкции языка basic
а потом написать интерпретатор, который будет содержать такие функции как
check_loop, check_if и тому подобное.

Остальные тэги тоже придеться разбирать уже на стадии интерпретатора, чтобы допустить вложения тэга basic.

[url]
[basic]
IF чтото
    PRINT url1
ELSE
    PRINT url2
[/basic]
[/url]

Обратной вложенности я так понимаю нам не нужно.

То есть невозможно сделать чтонибудь типа:

[basic]
    FOR i step 1
        [img]блаблабла_i[/img]
[/basic]

В рамках описанного такое,вроде, невозможно.