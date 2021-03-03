pref = input('What is your temp measured in? Celcius or Fahrenheit?: ')

temp = input('Enter temperature: ')
temp_float = float(temp)
conv_to_c = (temp_float - 32) * 0.5556
conv_to_f = (temp_float * 1.8) + 32

if pref == 'Celcius' or pref == 'celcius':
    print('Your temperature is', conv_to_f, 'degrees Fahrenheit')
elif pref == 'Fahrenheit' or pref == 'fahrenheit':
    print('Your temperature is', conv_to_c, 'degrees Celcius')