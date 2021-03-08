def arithmetic_arranger(problems, optional=False):

    problem_dict = dict()
  
    for problem in problems: 
        ps = problem.split()
        prolem_dict[ps] = (int(ps[0]), (ps[1], int(ps[2]))
        

    return problem_dict

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
