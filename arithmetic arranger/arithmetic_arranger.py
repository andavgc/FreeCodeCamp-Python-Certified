def arithmetic_arranger(list, show_result=False):

    if len(list) > 5:
        raise TypeError("Too many problems.")
    #separating elements
    op_list = []
    for x in list:
        operation = operation_separator(x)
        if "+" in x:
            r = operation[0] + operation[1]
        else:
            r = operation[0] - operation[1]
        operation.append(r)
        op_list.append(operation)
    #formatting elements
    primeira_linha = ''
    segunda_linha = ''
    terceira_linha = ''
    quarta_linha = ''
    i = 1
    for op in op_list:
        operand_1 = op[0]
        operand_2 = op[1]
        operator = op[2]
        result = op[3]
        length = max(len(str(operand_1)), len(str(operand_2)))

        if i == len(op_list):
            primeira_linha += f"{operand_1:>{length+2}}"
            segunda_linha += f"{operator} {operand_2:>{length}}"
            terceira_linha += f"{'-' * (length + 2)}"
            quarta_linha += f"{result:>{length+2}}"
        else:
            primeira_linha += f"{operand_1:>{length+2}}    "
            segunda_linha += f"{operator} {operand_2:>{length}}    "
            terceira_linha += f"{'-' * (length + 2)}    "
            quarta_linha += f"{result:>{length+2}}    "
        i += 1
        # join every arithmetic operation together
        #final_result = f''
    if show_result == False:
        print(f"{primeira_linha}\n"
              f"{segunda_linha}\n"
              f"{terceira_linha}"
              )
    else:
        print(f"{primeira_linha}\n"
              f"{segunda_linha}\n"
              f"{terceira_linha}\n"
              f"{quarta_linha}"
              )


def operation_separator(x):
    error = 'error'
    if "+" in x:
        operands = x.split(" + ")
        operands.append("+")
    elif "-" in x:
        operands = x.split(" - ")
        operands.append("-")
    else:
        raise TypeError("Operator must be '+' or '-'")
    i = 0
    for number in operands:
        try:
            operands[i] = int(number)
            i += 1
            if len(number) > 4:
                raise TypeError("Numbers cannot be more than four digits.")
            if i == 2:
                break
        except:
            raise TypeError("Numbers must only contain digits.")
    return operands