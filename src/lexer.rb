class Lexer
  def initialize(string)
    @string = string
    @current_position = 0
    @int_re = /\d+/
    @tokens = ["(", ")", '"', " ", "+", "-", "*", "/"]
    @keywords = ["printf", "eval"]
  end

  def tokenize
    actual_tokens = []
    print_tokens = []
    nums = []
    curr_number = 0
    data = @string.chars
    for i in data
      if i.match?(@int_re)
        curr_number = @current_position
        while curr_number < data.size and data[curr_number].match?(@int_re)
          nums.append(data[curr_number])
          curr_number += 1
        end
        actual_tokens.append(nums.join(""))
        print_tokens.append("[NUMBER: #{nums.join("")}]")
        nums = []
      end
      for j in @tokens
        if i == j
          actual_tokens.append(i)
          print_tokens.append("[TOKEN: #{i}]")
        end
      end
      @current_position += 1
    end
    puts print_tokens
    return actual_tokens
  end
end
