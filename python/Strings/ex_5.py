# Make a program that grabs the numbers and convert to a float.  

text = 'X-DSPAM-Confidence:0.8475'

colon = text.find(':')
numbers = text [colon + 1:]
done = float(numbers.strip())
print(done)