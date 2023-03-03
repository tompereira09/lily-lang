class Tokenizer
  def initialize
    @curr_pos = 0
    @re =
      / (?<number>\d++)
      | (?<word>\w++)
      | (?<token>[()+\-*\/'"'])
      | (?<linebreak>\R++)
      | (?<whitespace>\s++)
      | . # anything else
      /x
    @tokens = []

  def tokenize(line)
    line.scan(@re) do
      case
        when i = $~[:number]
          @tokens.append(i)
          puts "[NUMBER: #{i}]"
        when i = $~[:word]
          @tokens.append(i)
          puts "[WORD: #{i}]"
        when i = $~[:token]
          @tokens.append(i)
          puts "[TOKEN: #{i}]"
        when i = $~[:linebreak]
          tokens.append("\n")
        when i = $~[:whitespace]
          tokens.append(i)
          puts "[WHITESPACE]"
      else
        puts "No tokens found"
      end
    end
    return @tokens
  end 
end


tokenizer = Tokenizer.new()

code = "Hello, World"

puts tokenizer.tokenize(code)
