string_prompt = input('ENTER AN EQUATION').strip()
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
operator = ['(', ')', '+', '-', '*', '/', '^']
equation = []


def addition(n1, n2):
    return n2 + n1


def multiplication(n2, n1):
    return n2 * n1


def exponent(n1, n2):
    return n1 ** n2


dict_math = {"^": exponent,
             '*': multiplication,
             '+': addition,
             }


def string_to_list():
    number_to_be_added = ''
    for index, character in enumerate(string_prompt):
        if character in number:
            number_to_be_added += character
        if character in operator:
            if not number_to_be_added == '':
                equation.append(float(number_to_be_added))
            if character == '(':
                if len(equation) is not 0:
                    if type(equation[-1]) == float or equation[-1] == ')':
                        equation.append("*")
            equation.append(character)
            number_to_be_added = ''
    if not number_to_be_added == '':
        equation.append(float(number_to_be_added))


def correct_equation():
    for index, character in enumerate(equation):
        if character == '-':
            if type(equation[index + 1]) == float:
                equation.pop(index)
                if not equation[index - 1] in operator and not index == 0 or equation[index - 1] == ')':
                    equation.insert(index, '+')
                    equation[index + 1] = equation[index + 1] * -1
                else:
                    equation[index] = equation[index] * -1
        if character == '/':
            if type(equation[index + 1]) == float:
                equation.pop(index)
                equation.insert(index, '*')
                equation[index + 1] = equation[index + 1] ** -1


def solve(given_equation):
    print(given_equation)
    for operation in dict_math:
        check = False
        while not check:
            for index, character in enumerate(given_equation):
                if character == operation:
                    x = round(dict_math[operation](given_equation[index - 1], given_equation[index + 1]), 10)
                    for c in range(0, 3):
                        given_equation.pop(index - 1)
                    given_equation.insert(index - 1, x)
                    check = False
                    break
                else:
                    check = True
    print(given_equation)
    return given_equation[0]


def isolate_bracket():
    equation_within_brakcet = []
    left_bracket_index = 0
    right_bracket_index = 0
    list_of_bracket_index = []
    bracket_present_flag = False
    for index, character in enumerate(equation):
        if character == ')':
            right_bracket_index = index
            counter = index - 1
            while not counter < 0:
                if equation[counter] == '(' and counter not in list_of_bracket_index:
                    left_bracket_index = counter
                    list_of_bracket_index.append(counter)
                    bracket_present_flag = True
                    break
                else:
                    counter += - 1
            break
    if bracket_present_flag:
        for index in range(left_bracket_index + 1, right_bracket_index):
            equation_within_brakcet.append(equation[index])

        for index in range(left_bracket_index, right_bracket_index + 1):
            equation.pop(left_bracket_index)
        equation.insert(left_bracket_index, solve(equation_within_brakcet))
        correct_equation()
        isolate_bracket()
    else:
        solve(equation)


string_to_list()
correct_equation()
print(equation)
isolate_bracket()
print(round(equation[0], 4))
