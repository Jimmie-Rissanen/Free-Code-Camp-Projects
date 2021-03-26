
the_list = ["32 + 698", "3801 - 2", "5067 + 3", "123 + 6449"]
first_row = ''
second_row = ''
third_row = ''
answer_row = ''

for item in the_list:
    things = item.split()
    big = max(things)
    width = len(big) + 2
    dash = '-' * width
    first_row += '{first:>{w}}    '.format(first = things[0], w = width)
    second_row += '{op}{second:>{w}}    '.format(op = things[1], second = things[2], w = width - 1)
    third_row += '{dash:>{w}}    '.format(dash = dash, w = width)
print(first_row)
print(second_row)
print(third_row)