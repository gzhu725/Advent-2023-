#search for symbols
#any number next to a symbol is a part number
#sum  up
p1 = 0 
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

with open('input3.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]


#file formatting...
formatted_lines = []
for line in lines:
  line = line.split(" ")
  formatted_lines.append(line)
print(formatted_lines)