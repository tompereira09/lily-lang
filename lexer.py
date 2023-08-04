class Token:
    def __init__(self) -> None:
        self.value = ""
        self.type = ""

class Tokenizer:
    def __init__(self):
        self.nums = [0,1,2,3,4,5,6,7,8,9]
        self.ret_tokens = []
        self.lits = ["+", "-", "/", "*"]
        self.cont_index = 0
        self.curr_num = ""

    def isNumeric(self, char):
        numbers = ["0","1","2","3","4","5","6","7","8","9"]
        if char in numbers:
            return True
        else:
            return False

    def peekNext(self, tokens, curr_index):
        return tokens[curr_index + 1]

    def tokenize(self, file_name):
        contents = open(file_name, "r").read()
        for i in contents:
            curr_token = Token()
            curr_token.value = i
            if self.isNumeric(i):
                curr = contents.index(i)
                while self.isNumeric(contents[curr]):
                    self.curr_num += contents[curr]
                    curr += 1

                curr_token.type = "INT"
                curr_token.value = int(self.curr_num)
                self.ret_tokens.append(curr_token)
                self.curr_num = ""
                curr = contents.index(i)
            elif i in self.lits:
                curr_token.type = "LITERAL"
                self.ret_tokens.append(curr_token)
                self.cont_index += 1
            elif i == ";":
                curr_token.type = "SC"
                self.ret_tokens.append(curr_token)
                self.cont_index += 1
            else:
                if i == " " or i == "\n":
                    self.cont_index += 1
                    pass
        return self.ret_tokens