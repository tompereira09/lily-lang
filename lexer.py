import string
import json

jsonconts = open("manifest.json", "r").read()
jsonconts = json.loads(jsonconts)


class Lexer:
    def __init__(self):
        self.curr_line = 1
        self.curr_char = ''
        self.literals = list(jsonconts["literals"])
        self.string = list(string.ascii_lowercase+string.ascii_uppercase+"!#$%&?@€,.;:-_^`´<>"+" ")
        self.nums = [1,2,3,4,5,6,7,8,9,0]
        self.keywords = jsonconts["keywords"]
        self.temp_str = ""
        self.temp_keyword = ""
        self.inside_str = False
        self.tokens = []

    def tokenize(self, file):
        contents = open(file, "r").read()

        for curr_line in contents:
            for self.curr_char in curr_line:
                if self.temp_keyword in self.keywords:
                    self.tokens.append((self.temp_keyword, "KEYWORD"))
                    self.temp_keyword = ""
                else:
                    if self.curr_char in self.literals:
                        if self.curr_char != "'":
                            self.tokens.append((self.curr_char, "LITERAL"))
                        else:
                            if self.inside_str == True:
                                self.tokens.append((self.temp_str, "STRING"))
                                self.temp_str = ""
                                self.inside_str = False
                            else:
                                self.inside_str = True
                    else:
                        if self.curr_char != '\n':
                            if self.curr_char in self.string:
                                if self.inside_str == False:
                                    self.temp_keyword += self.curr_char
                                else:
                                    self.temp_str += self.curr_char
                            else:
                                try:
                                    if self.curr_char != "'":
                                        if int(self.curr_char) in self.nums:
                                            if self.inside_str == False:
                                                self.tokens.append((self.curr_char, "NUMBER"))
                                            else:
                                                self.temp_str += self.curr_char
                                        else:
                                            print(f'Error at line: {self.curr_line}, at char: {self.curr_char}')
                                    else:
                                        if self.inside_str == True:
                                            self.tokens.append((self.temp_str, "STRING"))
                                            self.temp_str = ""
                                            self.inside_str = False
                                        else:
                                            self.inside_str = True
                                except Exception as e:
                                    print(f'Python Error: {e}')
            self.curr_line += 1

        return self.tokens
