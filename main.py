import lexer
import astgen

file = input("filename: ")
tokenizer = lexer.Tokenizer()

tokens = tokenizer.tokenize(file)
parser = astgen.Parser()
for i in parser.parse(tokens):
	print(f'{i.left.token.value} {i.token.value} {i.right.token.value}')
