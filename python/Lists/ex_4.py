romeo = '''But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief'''

#fhand = open('romeo.txt')

unique = []

a = romeo.split()

for i in a:
    if i not in unique:
        unique.append(i)
unique.sort()
print(unique)
