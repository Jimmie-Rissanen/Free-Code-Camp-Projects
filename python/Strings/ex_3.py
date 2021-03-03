# Make a counting loop that is defiend in a function
#Count had to be a local variable
def count_letter(string, letter):
    count = 0
    for i in string:
        if i == letter:
            count = count + 1
    print(count)

stringi = input('Enter text: ')
lettero = input('What letter do you want to look for? ')
#stringi = 'hello'
#lettero = 'l'
count_letter(stringi, lettero)
