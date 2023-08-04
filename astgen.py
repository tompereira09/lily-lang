class AST_NODE:
    def __init__(self, token_to_ass):
        self.token = token_to_ass
        self.left = None
        self.right = None


class Parser:
    def __init__(self):
        self.curr_node = None
        self.curr_op = None
        self.sc_to_app = False
        self.ret = []

    def parse(self, tokens):
        for i in range(len(tokens)):
            self.curr_node = AST_NODE(tokens[i])
            if self.curr_node.token.type == "INT":
                if self.curr_op != None:
                    if self.curr_op.left == None:
                        self.curr_op.left = self.curr_node
                    elif self.curr_op.left != None:
                        if self.curr_op.right == None:
                            self.curr_op.right = self.curr_node
                else:
                    self.curr_to_app = self.curr_node
            elif self.curr_node.token.type == "LITERAL":
                self.curr_op = self.curr_node
                if self.curr_to_app != None:
                    self.curr_op.left = self.curr_to_app
            elif self.curr_node.token.type == "SC":
                self.sc_to_app = True
            if self.sc_to_app == True:
                self.ret.append(self.curr_op)
                self.curr_op = None
                self.sc_to_app = False

        return self.ret
