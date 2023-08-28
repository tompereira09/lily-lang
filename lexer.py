class Token:
    def __init__(self) -> None:
        self.value = ""
        self.type = ""

class Tokenizer:
    def __init__(self):
        self.ret_tokens = []
        self.lits = ["+", "-", "/", "*", "(", ")"]
        self.specials = ["#"]
        self.curr_comment = ""
        self.cont_index = 0
        self.on_comment = False
        self.curr_num = ""
        self.curr_kw = ""
        self.in_bxp = False

    def peekNext(self, tokens, curr_index):
        return tokens[curr_index + 1]

    def tokenize(self, contents):
        def is_ident_character(c, first):
            if first:
                return c.isalpha() or c == "_"
            else:
                # Identifiers can have numbers in them, just not as the first character
                return c.isalnum() or c == "_"

        for curr_char in range(len(contents)):
            i = contents[curr_char]
            if self.on_comment == True:
                if i != "#":
                    self.curr_comment += i
                else:
                    self.on_comment = False
                    curr_token.type = "COMMENT"
                    curr_token.value = self.curr_comment
                    self.ret_tokens.append(curr_token)
                    self.curr_comment = ""
            else:
                curr_token = Token()
                curr_token.value = i

                if i.isnumeric():
                    while contents[curr_char].isnumeric():
                        self.curr_num += contents[curr_char]
                        curr_char += 1

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
                elif i in self.specials:
                    if i == "#":
                        if self.on_comment == False:
                            self.on_comment = True
                elif is_ident_character(i, True) and self.on_comment == False:
                    while is_ident_character(i, False):
                        self.curr_kw += i
                        curr_char += 1
                        i = contents[curr_char]

                    if self.curr_kw == "print":
                        curr_token.type = "IDENT"
                        curr_token.value = "KW_PRINT"
                        self.ret_tokens.append(curr_token)

                        # The comment bellow was debug stuff

                        #if curr_token in self.ret_tokens:
                            #print("Returned print")
                        curr_token = None
                        self.curr_kw = ""

                else:
                    if i == " " or i == "\n":
                        self.cont_index += 1
                        pass

        return self.ret_tokens

