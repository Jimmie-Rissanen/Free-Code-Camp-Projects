def compute_grade(score):
    if score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    elif score < 0.6:
        print('F')

try:
    score = float(input('Enter score: '))
except: 
    print('Bad score')
    quit()

compute_grade(score)