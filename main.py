import lexer
import astgen
import translator
import os

to_parse = False

file = input("filename: ")
ans = input("ManualCompilation?(y/n)\n")
print("\n\nOutput: ---------------------")
if ans == "y":
    to_parse = True
elif ans == "n":
    to_parse = False
else:
    to_parse = False
tokenizer = lexer.Tokenizer()

tokens = tokenizer.tokenize(file)
parser = astgen.Parser()
parsed = parser.parse(tokens)
#for i in parser.parse(tokens):
#	print(f'{i.left.token.value} {i.token.value} {i.right.token.value}')
translator = translator.Translator()
translated = translator.translate(parsed, file)

if to_parse == True:
    os.system(f'gcc {file[:-3]}.c')
    os.system("./a.out")


