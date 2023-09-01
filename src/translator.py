class Translator:

    def translate(self, nodes, filename):
        output = open(filename[:-3]+".c", "w")
        output.write("#include <stdio.h>\n\n")
        output.write("int main() {\n")
        variables = []

        for i in range(len(nodes)):
            curr_Node = nodes[i]
            if hasattr(curr_Node, "type") and curr_Node.type == "Binary_Exp":
                match curr_Node.token.value:
                    case "+":
                        output.write(f'\tprintf("%d\\n", {curr_Node.left.token.value} + {curr_Node.right.token.value});\n')
                    case "-":
                        output.write(f'\tprintf("%d\\n", {curr_Node.left.token.value} - {curr_Node.right.token.value});\n')
                    case "*":
                        output.write(f'\tprintf("%d\\n", {curr_Node.left.token.value} * {curr_Node.right.token.value});\n')
                    case "/":
                        output.write(f'\tprintf("%d\\n", {curr_Node.left.token.value} / {curr_Node.right.token.value});\n')
            elif hasattr(curr_Node, "type") and curr_Node.type == "Str_Comment":
                output.write(f'\t//{curr_Node.token.value}\n')
            elif hasattr(curr_Node, "type") and curr_Node.type == "Print_Kw":
                output.write(f'\tprintf({curr_Node.parse_args});\n')
            elif hasattr(curr_Node, "type") and curr_Node.type == "SetMem_Kw":
                output.write(f'\t*((int *){curr_Node.mem_addr}) = {curr_Node.value_to_assign};\n')
            elif hasattr(curr_Node, "type") and curr_Node.type == "Var_Kw":
                if curr_Node.name not in variables:
                    match curr_Node.data_type:
                        case "int":
                            output.write(f'\tint{curr_Node.name} = {curr_Node.parse_value};\n')
                            variables.append(curr_Node.name)
                        case "float":
                            variables.append(curr_Node.name)
                            output.write(f'\tfloat{curr_Node.name} = {curr_Node.parse_value};\n')
                        case "str":
                            variables.append(curr_Node.name)
                            output.write(f'\tchar*{curr_Node.name} = "{curr_Node.parse_value}";\n')
                else:
                    match curr_Node.data_type:
                        case "int":
                            output.write(f'\t{curr_Node.name[1:]} = {curr_Node.parse_value};\n')
                        case "float":
                            output.write(f'\t{curr_Node.name[1:]} = {curr_Node.parse_value};\n')
                        case "str":
                            output.write(f'\t{curr_Node.name[1:]} = "{curr_Node.parse_value}";\n')
        output.write("\treturn 0;\n")
        output.write("}\n")




