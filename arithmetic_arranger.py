def arithmetic_arranger(problems, solution=False):
    arranged_problems = ''
    if len(problems) > 5:
        return "Error: Too many problems."

    operators = list(map(lambda x: x.split()[1], problems))
    for i in range(len(operators)):
        if operators[i] != '+' and operators[i] != '-' and operators[i] != 2:
            return "Error: Operator must be '+' or '-'."

    numbers = [] 
    for i in problems:
        number = i.split()
        numbers.extend([number[0], number[2]])

    if not all(map(lambda x: x.isdigit(), numbers)):
        return "Error: Numbers must only contain digits."

    if not all(map(lambda x: len(x) < 5, numbers)):
        return "Error: Numbers cannot be more than four digits."

    firstnumber = ''
    dashes = ''
    values = list(map(lambda x: eval(x), problems))
    solutions = ''
    for i in range(0, len(numbers), 2):
        space_width = max(len(numbers[i]), len(numbers[i+1])) + 2
        firstnumber += numbers[i].rjust(space_width)
        dashes += '-' * space_width
        solutions += str(values[i // 2]).rjust(space_width)
        if i != len(numbers) - 2:
            firstnumber += ' ' * 4
            dashes += ' ' * 4
            solutions += ' ' * 4

    secondnumber = ''
    for i in range(1, len(numbers), 2):
        space_width = max(len(numbers[i - 1]), len(numbers[i])) + 1
        secondnumber += operators[i // 2]
        secondnumber += numbers[i].rjust(space_width)
        if i != len(numbers) - 1:
            secondnumber += ' ' * 4

    if solution:
        arranged_problems = '\n'.join((firstnumber, secondnumber, dashes, solutions))
    else:
        arranged_problems = '\n'.join((firstnumber, secondnumber, dashes))
    return arranged_problems