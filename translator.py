class Translator:
    def __init__(self):
        self.curr_Node = None

    def translate(self, nodes, filename):
        output = open(filename[:-3]+".c", "w")
        output.write("#include <stdio.h>\n")
        output.write("int main() {\n")
        output.write("\tint a;\n")
        output.write("\tint b;\n")
        output.write("\tint c;\n")

        for i in range(len(nodes)):
            self.curr_Node = nodes[i]
            output.write(f'\ta = {self.curr_Node.left.token.value};\n')
            output.write(f'\tb = {self.curr_Node.right.token.value};\n')
            match self.curr_Node.token.value:
                case "+":
                    output.write("\tc = a + b;\n")
                case "-":
                    output.write("\tc = a - b;\n")
                case "*":
                    output.write("\tc = a * b;\n")
                case "/":
                    output.write("\tc = a / b;\n")

            output.write(f'\tprintf("%d\\n", c);\n')

        output.write("\treturn 0;\n")
        output.write("}\n")




