# frozen_string_literal: true

class Lexer
  REGEXP =
    / (?<number>\d++)
    | (?<word>\w++)
    | (?<token>[()+\-*\/"])
    | (?<linebreak>\R)
    | (?<whitespace>\s)
    | . # anything else
    /x
  KEYWORDS = %w[printf eval]

  def initialize(string)
    @string = string
  end

  def tokenize
    actual_tokens = []
    @string.scan(REGEXP) do
      warn(
        case
          when i = $~[:number]
            actual_tokens << i
            "[NUMBER: #{i}]"
          when i = $~[:word]
            # TODO: `KEYWORDS`
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
