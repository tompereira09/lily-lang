import sys
import lexer #Temporary because it will be later passed to the parser

file_path = sys.argv[1]

lex_obj = lexer.Lexer()
for i in lex_obj.tokenize(file_path):
    print(i)
