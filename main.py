import lexer
import astgen
import translator

file = input("filename: ")
tokenizer = lexer.Tokenizer()

tokens = tokenizer.tokenize(file)
parser = astgen.Parser()
parsed = parser.parse(tokens)
#for i in parser.parse(tokens):
#	print(f'{i.left.token.value} {i.token.value} {i.right.token.value}')
translator = translator.Translator()
translated = translator.translate(parsed, file)
