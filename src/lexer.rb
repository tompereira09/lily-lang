# frozen_string_literal: true

class Lexer
  def initialize(string)
    @string = string
    @current_position = 0
    @re =
      / (?<number>\d++)
      | (?<word>\w++)
      | (?<token>[()+\-*\/"])
      | (?<linebreak>\R++)
      | (?<whitespace>\s++)
      | . # anything else
      /x
    @keywords = ["printf", "eval"]
  end

  def tokenize
    actual_tokens = []
    @string.scan(@re) do
      warn(
        case
          when i = $~[:number]
            actual_tokens << i
            "[NUMBER: #{i}]"
          when i = $~[:word]
            # TODO: @keywords
          when i = $~[:token]
            actual_tokens << i
            "[TOKEN: #{i}]"
          when $~[:linebreak]
            # TODO: ?
          when $~[:whitespace]
            # TODO: ignore?
        else
          # TODO: raise error
        end
      )
    end
    actual_tokens
  end
end
