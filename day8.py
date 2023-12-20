
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

#naive way was not efficietn enough...needed help to identify this was an LCM PRoblem
#credit: hyper neutrino 
'''
a_nodes = list()
found_z = [False] * 6
lol = [True, True, True, True, True, True]
p2 = 0
for key in locations.keys():
  if(key[-1] == 'A'):
    a_nodes.append(key)
#while we haven't gotten all Z  values
while(found_z != lol):
  current_direction = instruction[p2 % len(instruction)]
  for i in range(len(a_nodes)):
    current_node = a_nodes[i]
    next_node = None
    if(current_direction == 'L'):
      next_node = lines[locations[a_nodes[i]]][7:10]
    elif(current_direction == 'R'):
      next_node = lines[locations[a_nodes[i]]][12:15]
    if(current_node[-1] == 'Z'):
      found_z[i] = True
    elif(current_node[-1] != 'Z'):
      found_z[i] = False
    a_nodes[i] = next_node
  p2+=1
print(p2-1)
'''


##solution for part 2 bugging??? got from hyper neutrino
a_nodes = list()
for key in locations.keys():
  if(key[-1] == 'A'):
    a_nodes.append(key)
cycles = list()

for current in a_nodes:
    cycle = []

    current_steps = instruction
    step_count = 0
    first_z = None

    while True:
        while step_count == 0 or not current.endswith("Z"):
            step_count += 1
            if(current_steps == 'L'):
              current = lines[locations[current]][7:10]
            elif(current_steps == 'R'):
              next_node = lines[locations[current]][12:15]
            current_steps = current_steps[1:] + current_steps[0]

        cycle.append(step_count)

        if first_z is None:
            first_z = current
            step_count = 0
        elif current == first_z:
            break

    cycles.append(cycle)

nums = [cycle[0] for cycle in cycles]

lcm = nums.pop()

for num in nums:
    lcm = lcm * num // gcd(lcm, num)

print(lcm)