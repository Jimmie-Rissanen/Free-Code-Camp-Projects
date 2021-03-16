def arithmetic_arranger(problems, optional=True):
    # Lists that contian the answeres.
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

        if not first.isdigit() or not second.isdigit():
            return 'Error: Numbers must only contain digits.'
        # Get the length and align the problem.
        if op == '+':
            solution = int(first) + int(second)
        elif op == '-':
            solution = int(first) + int(second)
        elif not op == '+' or not op == '-': 
            return "Error: Operator must be '+' or '-'."
        solution = str(solution)
        length = len(max(problem))
        if length > 4:
            return 'Error: Numbers cannot be more than four digits.'
        dashes = '-' * length
            
        #Return different lists depending on true or false.   
        if optional is True:
            stacked = f"{first.rjust(6)}\n{op}{second.rjust(5)}\n{dashes.rjust(5)}\n{solution.rjust(5)}"
            stacked.strip()
            answers.append(stacked)
        else:
            stacked = f"{first.rjust(6)}\n{op}{second.rjust(5)}\n{dashes.rjust(5)}"
            stacked.strip()
            answers.append(stacked)
    print("    ".join(answers))
    
         
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 443", "123 + 449"])