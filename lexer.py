import string
import json

jsonconts = open("manifest.json", "r").read()
jsonconts = json.loads(jsonconts)


class Lexer:
    def __init__(self):
        self.curr_line = 1
        self.curr_char = ''
        self.literals = list(jsonconts["literals"])
        self.string = list(string.ascii_lowercase+string.ascii_uppercase+"!#$%&?@€,.;:-_^`´<>")
        self.nums = [1,2,3,4,5,6,7,8,9,0]
        self.temp_str = ""
        self.tokens = []

    def tokenize(self, file):
        contents = open(file, "r").read()

        for curr_line in contents:
            for self.curr_char in curr_line:
                if self.curr_char in self.literals:
                    self.tokens.append((self.curr_char, "LITERAL"))
                else:
                    if self.curr_char != '\n' and self.curr_char != ' ':  # Changed 'or' to 'and' in the condition
                        if self.curr_char in self.string:
                            self.tokens.append((self.curr_char, "CHAR"))
                        else:
                            try:
                                if int(self.curr_char) in self.nums:
                                    self.tokens.append((self.curr_char, "NUMBER"))
                                else:
                                    print("Error at line", self.curr_line, "at char:", self.curr_char)
                            except Exception as e:
                                print("Python Error:", e)
            self.curr_line += 1

        return self.tokens
