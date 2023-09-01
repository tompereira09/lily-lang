class Token:
    def __init__(self) -> None:
        self.value = ""
        self.type = ""
        self.belongs_to_print = False
        self.line = 0

class Tokenizer:
    def __init__(self):
        self.ret_tokens = []
        self.lits = ["+", "-", "/", "*", "(", ")", "=", "[", "]", "{", "}"]
        self.specials = ["#"]
        self.curr_comment = ""
        self.cont_index = 0
        self.on_comment = False
        self.curr_num = ""
        self.curr_kw = ""
        self.curr_line = 0
        self.start_print = False
        #self.curr_p_expr = ""
        self.on_args = False
        self.start_setmem = False
        self.curr_args = ""
        self.start_assginement = False
        self.var_wait = False
        self.curr_var_val = ""
        self.curr_var_name = ""
        self.start_check = False
        self.curr_code_block = ""
        self.check_for_cb = False # Check for a code block
        self.on_statement = False

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
                curr_token.line = self.curr_line

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
                    if i == "(" or i == ")":
                        curr_token.type = "LITERAL"
                        self.ret_tokens.append(curr_token)
                        if self.start_print and i == "(":
                            self.on_args = True
                            while i != ")":
                                self.curr_args += i
                                curr_char += 1
                                i = contents[curr_char]
                            self.curr_args = self.curr_args[1:]
                            curr_token.type = "PRINT_ARGS"
                            curr_token.value = self.curr_args
                            self.ret_tokens.append(curr_token)
                            curr_token = None
                            self.curr_args = ""
                            self.start_print = False
                        elif self.start_setmem and i == "(":
                            self.on_args = True
                            while i != ")":
                                self.curr_args += i
                                curr_char += 1
                                i = contents[curr_char]
                            self.curr_args = self.curr_args[1:]
                            curr_token.type = "SETMEM_ARGS"
                            curr_token.value = self.curr_args
                            self.ret_tokens.append(curr_token)
                            curr_token = None
                            self.curr_args = ""
                            self.start_setmem = False

                    elif i == "=":
                        curr_token.type = "ASSIGNEMENT"
                        self.ret_tokens.append(curr_token)
                        self.cont_index += 1
                        if self.var_wait:
                            while i != ";":
                                self.curr_var_val += i
                                curr_char += 1
                                i = contents[curr_char]
                            curr_token.type = "ASS_VAL"
                            curr_token.value = self.curr_var_val
                            self.ret_tokens.append(curr_token)
                            self.curr_var_val = ""
                            self.var_wait = False
                    elif i == "[":
                        if self.start_check:
                            curr_token.type = "IF_ARGS"
                            while i != "]":
                                self.curr_args += i
                                curr_char += 1
                                i = contents[curr_char]
                            curr_token.value = self.curr_args[1:]
                            self.ret_tokens.append(curr_token)
                            self.curr_args = ""
                            self.start_check = False
                            self.check_for_cb = True
                    elif i == "{":
                        if self.check_for_cb:
                            while i != "}" and self.curr_args == "":
                                self.curr_code_block += i
                                curr_char += 1
                                if curr_char < len(contents):
                                    i = contents[curr_char]
                                else:
                                    break
                            curr_token.type = "CB"
                            curr_token.value = self.curr_code_block[2:]
                            self.ret_tokens.append(curr_token)
                            self.curr_code_block = ""
                        else:
                            curr_token.type = "LITERAL"
                            self.ret_tokens.append(curr_token)
                            self.cont_index += 1
                    else:
                        curr_token.type = "LITERAL"
                        self.ret_tokens.append(curr_token)
                        self.cont_index += 1
                elif i == ";":
                    curr_token.type = "SC"
                    self.ret_tokens.append(curr_token)
                    self.cont_index += 1
                    if self.on_args == True:
                        self.on_args = False

                elif i in self.specials:
                    if i == "#":
                        if self.on_comment == False:
                            self.on_comment = True
                elif is_ident_character(i, True) and self.on_comment == False and self.on_args == False:
                    #print(self.on_args)
                    while is_ident_character(i, False):
                        #print(i, self.on_args)
                        self.curr_kw += i
                        curr_char += 1
                        i = contents[curr_char]

                    if self.curr_kw == "print":
                        self.on_args = True
                        #print(self.on_args)
                        curr_token.type = "IDENT"
                        curr_token.value = "KW_PRINT"
                        self.ret_tokens.append(curr_token)
                        self.start_print = True

                        # The comment bellow was debug stuff

                        #if curr_token in self.ret_tokens:
                            #print("Returned print")
                        curr_token = None
                        self.curr_kw = ""
                    elif self.curr_kw == "setmem":
                        self.on_args = True
                        #print(self.on_args)
                        curr_token.type = "IDENT"
                        curr_token.value = "KW_SETMEM"
                        self.ret_tokens.append(curr_token)
                        self.start_setmem = True
                        curr_token = None
                        self.curr_kw = ""
                    elif self.curr_kw == "var":
                        self.on_args = True
                        #print("Found var")
                        curr_token.type = "IDENT"
                        curr_token.value = "KW_VAR"
                        self.ret_tokens.append(curr_token)
                        curr_token = None
                        while contents[curr_char + 1] != "=":
                                self.curr_var_name += i
                                curr_char += 1
                                i = contents[curr_char]
                        curr_token = Token()
                        curr_token.type = "IDENT"
                        curr_token.value = self.curr_var_name
                        self.ret_tokens.append(curr_token)
                        curr_token = None
                        self.curr_kw = ""
                        self.curr_var_name = ""
                        self.var_wait = True
                    elif self.curr_kw == "check":
                        self.on_args = True
                        #print(self.on_args)
                        curr_token.type = "IDENT"
                        curr_token.value = "KW_CHECK"
                        self.ret_tokens.append(curr_token)
                        self.start_check = True

                    else:
                        #print("Found IDENT")
                        curr_token.type = "IDENT"
                        curr_token.value = self.curr_kw
                        self.ret_tokens.append(curr_token)
                        curr_token = None
                        self.curr_kw = ""
                else:
                    if i == " " or i == "\n":
                        if i == "\n":
                            self.curr_line += 1
                        else:
                            pass

        return self.ret_tokens

