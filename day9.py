last_numbers = []
all_differences = []
backwards_sums = []
for line in open('input9.txt'):
  line = line.strip().split(' ')
  line = [int(x) for x in line] # line with each int separated
  different_list = list(line) #start with original line
  all_differences.append(list(different_list))
  last_numbers.append([]) #last number for original line
  while(len(different_list) == 0 or not all(i == 0 for i in different_list)):
    for i in range(len(different_list)-1):
      different_list[i]= different_list[i+1] - different_list[i]
    last_numbers[-1].append(different_list.pop())
    #print(different_list)
    all_differences.append(list(different_list))
  for i in range(-2, -(len(all_differences) + 1), -1):
    #go backwards
    all_differences[i][0] = all_differences[i][0] - all_differences[i + 1][0]
  #print(all_differences)
  backwards_sums.append(all_differences[0][0])
  all_differences = []
p1 = 0
for value in last_numbers:
  cur_hist = sum(value)
  p1 += cur_hist
#print(p1)
p2 = sum(backwards_sums)
print(p2)
