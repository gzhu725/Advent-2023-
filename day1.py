import re 
with open('input1.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

#lines = all lines of the input
#PART 1
result = 0
for line in lines:
  for char in line:
    digits_only = ''.join(char for char in line if char.isdigit())
  number =  digits_only[0] + digits_only[-1]
  result += int(number)
#print(result)

#PART 2 - help of Jonathan Paulson's video 
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
p2 = 0
for line in lines:
  p2_digits = []
  for i,c in enumerate(line):
    if c.isdigit():
      p2_digits.append(c)
    for d,val in enumerate(numbers):
      if line[i:].startswith(val):
        p2_digits.append(str(d+1))
  p2 += int(p2_digits[0] + p2_digits[-1])
print(p2)





    








  
