require_relative "lexer"

data = File.readlines(ARGV[0])

for i in data
  tokenizer = Lexer.new(i)
  tokenizer.tokenize
end
