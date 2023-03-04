class Tokenizer
  def initialize
    @curr_pos = 0
    @re =
      / (?<number>\d++)
      | (?<word>\w++)
      | (?<token>[()+\-*\/'"',])
      | (?<linebreak>\R++)
      | (?<whitespace>\s++)
      | . # anything else
      /x
    @keywords = 
      / (?<int>"int")
      | (?<string>"string")
      | (?<float>"float")
      | (?<bool>"bool")
      | (?<print>"printf")
      | (?<eval>"eval")
      /x

    @keywords_check = ["int", "string", "float", "bool", "printf", "eval"]
    @tokens = []
  end

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
          @tokens.append("\n")
        when i = $~[:whitespace]
          @tokens.append(i)
          puts "[WHITESPACE]"
      else
        line.scan(@keywords) do
        case
          when i = $~[:int]
            @tokens.append(i)
            puts "[KEYWORD: #{i}]"
          when i = $~[:string]
            @tokens.append(i)
            puts "[KEYWORD: #{i}]"
          when i = $~[:float]
            @tokens.append(i)
            puts "[KEYWORD: #{float}"
          when i = $~[:bool]
            @tokens.append(i)
            puts "[KEYWORD: #{i}]"
          when i = $~[:print]
            @tokens.append(i)
            puts "[KEYWORD: #{i}]"
          when i = $~[:eval]
            @tokens.append(i)
            puts "[KEYWORD: #{i}]"
        else
          puts "No tokens found."
        end
        end
      end
    end
    return @tokens
  end 
end


tokenizer = Tokenizer.new()

code = "printf Hello, World"

tokens = tokenizer.tokenize(code)
