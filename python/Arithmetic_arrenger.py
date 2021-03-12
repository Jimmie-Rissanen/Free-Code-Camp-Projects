def arithmetic_arranger(problems, optional=False):
     
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for problem in problems:
        problem = problem.split()
        first = problem[0]
        op = problem [1]
        second = problem[2]
        if not first.isdigit() or not second.isdigit():
            return 'Error: Numbers must only contain digits.'
        if op == '+' or op == '-':
            length = len(max(problem))
            
        else: 
            return "Error: Operator must be '+' or '-'."
        
    return
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 443", "123 + 449"]))