class Translator:
    def __init__(self):
        self.curr_Node = None

    def translate(self, nodes, filename):
        output = open(filename[:-3]+".c", "w")
        output.write("#include <stdio.h>\n\n")
        output.write("int main() {\n")

        for i in range(len(nodes)):
            self.curr_Node = nodes[i]
            if self.curr_Node.type == "Binary_Exp":
                match self.curr_Node.token.value:
                    case "+":
                        output.write(f'\tprintf("%d\\n", {self.curr_Node.left.token.value} + {self.curr_Node.right.token.value});\n')
                    case "-":
                        output.write(f'\tprintf("%d\\n", {self.curr_Node.left.token.value} - {self.curr_Node.right.token.value});\n')
                    case "*":
                        output.write(f'\tprintf("%d\\n", {self.curr_Node.left.token.value} * {self.curr_Node.right.token.value});\n')
                    case "/":
                        output.write(f'\tprintf("%d\\n", {self.curr_Node.left.token.value} / {self.curr_Node.right.token.value});\n')
            elif self.curr_Node.type == "Str_Comment":
                output.write(f'\t//{self.curr_Node.token.value}\n')

        output.write("\treturn 0;\n")
        output.write("}\n")




