import re


def arithmetic_arranger(problems, answer=False):
    # Check the number of problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first = ""
    second = ""
    operator = ""
    lines = ""
    sum_problems = ""
    arranged_problems = ""

    for problem in problems:
        if (re.search("[^\s0-9.+-]", problem)):
          if (re.search("[/]", problem) or re.search("[*]", problem)):
            return "Error: Operator must be '+' or '-'."
          return "Error: Numbers must only contain digits."


        first_operand = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        second_operand = problem.split(" ")[2]

        if (len(first_operand) > 4 or len(second_operand) > 4):
          return "Error: Numbers cannot be more than four digits."

        sum = ""
        if (operator == "+"):
          sum = str(int(first_operand) + int(second_operand))
        elif (operator == "-"):
          sum = str(int(first_operand) - int(second_operand))

        length = max(len(first_operand), len(second_operand)) + 2
        top = str(first_operand).rjust(length)
        bottom = operator + str(second_operand).rjust(length - 1)

        line = ""
        
        result = str(sum).rjust(length)

        for dashes in range(length):
            line += "-"

        if problem != problems[-1]:
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            sum_problems += result + '    '
        else:
            first += top
            second += bottom
            lines += line
            sum_problems += result

    if answer:
        arranged_problems = first + "\n" + second + "\n" + lines + "\n" + sum_problems
    else:
        arranged_problems = first + "\n" + second + "\n" + lines

    return arranged_problems
