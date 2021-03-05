import string

fhand = open('romeo.txt')

counts = dict()

for line in fhand:
    line = line.translate(str.maketrans('','', string.punctuation))
    line.lower()
    words = line.split()
    for word in words:
        letters = word.split()
        for letter in letters:
            counts [letter] = counts.get(letter , 0) + 1

biggest = []

for key, value in counts.items():
    biggest.append((value, key))
biggest.sort(reverse= True)
for key, value in biggest:
    print(key, value)