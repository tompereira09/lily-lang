class Translator:

    def translate(self, nodes, filename):
        output = open(filename[:-3]+".c", "w")
        output.write("#include <stdio.h>\n\n")
        output.write("int main() {\n")

        for i in range(len(nodes)):
            curr_Node = nodes[i]
            if curr_Node.type == "Binary_Exp":
                match curr_Node.token.value:
                    case "+":
                        output.write(f'\tprintf("%d\\n", {curr_Node.left.token.value} + {curr_Node.right.token.value});\n')
                    case "-":
                        output.write(f'\tprintf("%d\\n", {curr_Node.left.token.value} - {curr_Node.right.token.value});\n')
                    case "*":
                        output.write(f'\tprintf("%d\\n", {curr_Node.left.token.value} * {curr_Node.right.token.value});\n')
                    case "/":
                        output.write(f'\tprintf("%d\\n", {curr_Node.left.token.value} / {curr_Node.right.token.value});\n')
            elif curr_Node.type == "Str_Comment":
                output.write(f'\t//{curr_Node.token.value}\n')
            elif curr_Node.type == "Print_Kw":
                output.write(f'\tprintf({curr_Node.parse_args});\n')
            elif curr_Node.type == "SetMem_Kw":
                output.write(f'\t*((int *){curr_Node.mem_addr}) = {curr_Node.value_to_assign};\n')

        output.write("\treturn 0;\n")
        output.write("}\n")




