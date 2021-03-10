def arithmetic_arranger(problems, optional=False):

    
    # Handle input

    # Compute 

    for problem in problems: 
        ps = problem.split()
        if ps[1] == "+":
            addition = int(ps[0]) + int(ps[2])
        if ps[1] == "-":
            addition = int(ps[0]) - int(ps[2])

    # Arrange problem

    return addition, subtraction

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print('hello')

