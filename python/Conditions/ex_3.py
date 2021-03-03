score = input('Enter score: ')

try: 
    scoref = float(score)
except:
    print('Bad score')
    quit()

if scoref >= 0.9 :
    print('A')
elif scoref >= 0.8:
    print('B')
elif scoref >= 0.7:
    print('C')
elif scoref >= 0.6:
    print('D')
elif scoref < 0.6:
    print('F')