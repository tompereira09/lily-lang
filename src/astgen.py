from lexer import Tokenizer
from translator import Translator

tokenizer = Tokenizer()
translator = Translator()

class AST_NODE:
    def __init__(self, token_to_ass):
        self.token = token_to_ass
        self.type = None
        self.left = None
        self.right = None
class PRINT_NODE:
    def __init__(self, token_to_ass):
        self.token = token_to_ass
        self.type = "Print_Kw"
        self.parse_args = ""

class SETMEM_NODE:
    def __init__(self, token_to_ass):
        self.token = token_to_ass
        self.type = "SetMem_Kw"
        self.parse_args = ""
        self.value_to_assign = None
        self.mem_addr = None

class VAR_NODE:
    def __init__(self, token_to_ass):
        self.token = token_to_ass
        self.type = "Var_Kw"
        self.parse_value = None
        self.data_type = None
        self.name = None

class CHECK_NODE:
    def __init__(self, token_to_ass):
        self.token = token_to_ass
        self.type = "Check_Statement"
        self.condition = None

class EO_BLOCK:
    def __init__(self, token_to_ass):
        self.token = token_to_ass
        self.type = "End_Of_Block"

class Parser:
    def __init__(self):
        self.curr_node = None
        self.curr_op = None
        self.curr_ret_token = None
        self.sc_to_app = False
        self.ret = []
        self.last_print = None
        self.last_setmem = None
        self.last_var = None
        self.last_check = None
        self.on_block = False

    def parse_mem_args(self, mem_args, line):
        addr = None
        value = None

        if ',' in mem_args:
            mem_args = mem_args.split(",")
            if "0x" in mem_args[0]:
                addr = mem_args[0]
            try:
                value = int(mem_args[1])
            except:
                print(f'Unsoported value for setmem, line {line}')
                quit()

            return [addr, value]

    def parse_var_value(self, var_args, line):
        value = None
        type = None

        if '"' not in var_args and "'" not in var_args:
            try:
                if "." not in var_args:
                    value = int(var_args)
                    type = "int"
                else:
                    value = float(var_args)
                    type = "float"
            except:
                print(f'Unsoported value for assignement, line {line}')
                quit()
        else:
            try:
                if '"' in var_args:
                    value = var_args.split('"')[1]
                    type = "str"
                elif "'" in var_args:
                    value = var_args.split("'")[1]
                    type = "str"
            except:
                print(f'Unsoported value for assignement, line {line}')
                quit()

        return [value, type]


    def parse(self, tokens):
        for i in range(len(tokens)):
            self.curr_node = AST_NODE(tokens[i])
            #print(self.curr_node.token.type) -> debug stuff
            if hasattr(self.curr_node.token, "type") and self.curr_node.token.type == "INT":
                if self.curr_op != None:
                    if self.curr_op.left == None:
                        self.curr_op.left = self.curr_node
                    elif self.curr_op.left != None:
                        if self.curr_op.right == None:
                            self.curr_op.right = self.curr_node
                else:
                    self.curr_to_app = self.curr_node
            elif hasattr(self.curr_node.token, "type") and self.curr_node.token.type == "LITERAL":
                if self.curr_node.token.value != "{" and self.curr_node.token.value != "}":
                    self.curr_op = self.curr_node
                    self.curr_op.type = "Binary_Exp"
                    if self.curr_to_app != None:
                        self.curr_op.left = self.curr_to_app
                else:
                    if self.curr_node.token.value == "}":
                        if self.on_block == True:
                            self.ret.append(EO_BLOCK(tokens[i]))
                            self.on_block = False
            elif hasattr(self.curr_node.token, "type") and self.curr_node.token.type == "IDENT":
                if self.curr_node.token.value == "KW_PRINT":
                    #print("Found Print")
                    self.last_print = PRINT_NODE(tokens[i])
                elif self.curr_node.token.value == "KW_SETMEM":
                    self.last_setmem = SETMEM_NODE(tokens[i])
                elif self.curr_node.token.value == "KW_VAR":
                    self.last_var = VAR_NODE(tokens[i])
                elif self.curr_node.token.value == "KW_CHECK":
                    print("Found keyword check")
                    self.last_check = CHECK_NODE(tokens[i])
                else:
                    # This won't work for long, add a type to the identifier so it works as normal
                    if self.last_var != None:
                        self.last_var.name = self.curr_node.token.value

            elif hasattr(self.curr_node.token, "type") and self.curr_node.token.type == "PRINT_ARGS":
                if self.last_print != None:
                    self.last_print.parse_args = self.curr_node.token.value
                    self.ret.append(self.last_print)
                    self.last_print = None
            elif hasattr(self.curr_node.token, "type") and self.curr_node.token.type == "SETMEM_ARGS":
                if self.last_setmem != None:
                    self.last_setmem.parse_args = self.curr_node.token.value
                    self.last_setmem.parse_args = self.parse_mem_args(self.last_setmem.parse_args, self.curr_node.token.line)
                    self.last_setmem.value_to_assign = self.last_setmem.parse_args[1]
                    self.last_setmem.mem_addr = self.last_setmem.parse_args[0]
                    self.ret.append(self.last_setmem)
                    self.last_setmem = None
            elif hasattr(self.curr_node.token, "type") and self.curr_node.token.type == "ASS_VAL":
                #print(self.curr_node.token.value)
                if self.last_var != "None":
                    if hasattr(self.last_var, "parse_value"):
                        self.last_var.parse_value = self.curr_node.token.value[1:]
                        self.last_var.data_type = self.parse_var_value(self.last_var.parse_value, self.curr_node.token.line)[1]
                        self.last_var.parse_value = self.parse_var_value(self.last_var.parse_value, self.curr_node.token.line)[0]
                        self.ret.append(self.last_var)
                        self.last_var = None
                else:
                    pass

            elif hasattr(self.curr_node.token, "type") and self.curr_node.token.type == "IF_ARGS":
                self.last_check.condition = self.curr_node.token.value
                self.ret.append(self.last_check)
                self.on_block = True
                self.last_check = None

            elif hasattr(self.curr_node.token, "type") and self.curr_node.token.type == "CB":
                print("Found CB")
                translator.translate(self.parse(tokenizer.tokenize(self.curr_node.token.value)), "file.ll")

            elif hasattr(self.curr_node.token, "type") and self.curr_node.token.type == "SC":
                self.sc_to_app = True
            elif hasattr(self.curr_node.token, "type") and self.curr_node.token.type == "COMMENT":
                self.curr_ret_token = self.curr_node
                self.curr_ret_token.type = "Str_Comment"
                self.ret.append(self.curr_ret_token)
            if self.sc_to_app == True:

                self.ret.append(self.curr_op)
                self.curr_op = None
                self.sc_to_app = False

        return self.ret
