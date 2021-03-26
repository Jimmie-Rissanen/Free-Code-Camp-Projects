def error_handling(problems):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    split_problems =  
    if item.isnumeric():
            continue
        elif item == '+' or item == '-':
            continue
            return 'Error: Numbers must only contain digits.'
        elif not op == '+' or not op == '-': 
        return "Error: Operator must be '+' or '-'."
        if length > 4:
        return 'Error: Numbers cannot be more than four digits.'

def arithmetic_arranger(problems, optional=True):
    # Lists that contian the answeres.
    first_row = ''
    second_row = ''
    third_row = ''
    answer_row = ''
    for item in problems:
        things = item.split()
        big = max(things)
        width = len(big) + 2
        dash = '-' * width
        first_row += '{first:>{w}}    '.format(first = things[0], w = width)
        second_row += '{op}{second:>{w}}    '.format(op = things[1], second = things[2], w = width - 1)
        third_row += '{dash:>{w}}    '.format(dash = dash, w = width)

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 443", "123 + 449"])