def arithmetic_arranger(problems, optional=True):
    # Lists that contian the answeres.
    num_row = ""
    op_row = ""
    dash_row = ""
    answere_row = ""
    sep = "    "
    answers = []
    if len(problems) > 5:
        return 'Error: Too many problems.'
    # Extract the relevant parts of the list.
    for problem in problems:
        problem = problem.split()
        first = problem[0]
        op = problem [1]
        second = problem[2]

        # Calculate to be able to show answere

        if not first.isnumeric() or not second.isnumeric():
            return 'Error: Numbers must only contain digits.'
        # Get the length and align the problem.
        if op == '+':
            solution = int(first) + int(second)
        elif op == '-':
            solution = int(first) + int(second)
        elif not op == '+' or not op == '-': 
            return "Error: Operator must be '+' or '-'."
        solution = str(solution)
        length = max(len(first), len(second)) 
        dashes = '-' * (length + 2)
        if length > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        num_row = '{:*>{width}}'.format(first, width=length)
        op_row = '{:*>{width}}'.format(op, width=length)
        dash_row = '{:*>{width}}'.format(second, width=length)          #testade output med hjälp av str.format()
        answere_row = '{:*>{width}}'.format(dashes, width=length)       #hur kan jag göra så att alla värden 
        print(num_row,op_row,dash_row,)                                 #kommer in utan hard coding? 
        print(answere_row)                                              # for loop och dictionary? 
    
    
         
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 443", "123 + 449"])