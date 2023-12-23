last_numbers = []
for line in open('input9.txt'):
  line = line.strip().split(' ')
  line = [int(x) for x in line] # line with each int separated
  different_list = list(line) #start with original line
  last_numbers.append([]) #last number for original line
  while(len(different_list) == 0 or not all(i == 0 for i in different_list)):
    for i in range(len(different_list)-1):
      different_list[i]= different_list[i+1] - different_list[i]
    last_numbers[-1].append(different_list.pop())
p1 = 0
for value in last_numbers:
  cur_hist = sum(value)
  p1 += cur_hist
print(p1)
