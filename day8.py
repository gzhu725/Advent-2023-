with open('input8.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

instruction = lines[0] #eg RL, LLR.. 
locations = dict() #eg, you can find AAA at index 1
for i in range(1, len(lines)):
  node = lines[i]
  specific_node = lines[i][0:3]
  locations[specific_node] = i
'''
current_node = 'AAA'
p1 = 0
#loop while we haven't reached the end
#part 1 
while(current_node != 'ZZZ'):
  current_direction = instruction[p1 % len(instruction)]
  if(current_direction == 'L'):
    current_node = lines[locations[current_node]][7:10]
  elif(current_direction == 'R'):
    current_node = lines[locations[current_node]][12:15]
  p1+=1

print(p1)
'''
a_nodes = list()
for key in locations.keys():
  if(key[-1] == 'A'):
    a_nodes.append(key)
print(a_nodes)