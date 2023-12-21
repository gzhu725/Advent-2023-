
with open('input19.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]
workflows = list()
parts = list()
hit_space = False
for line in lines:
  if(line == ''):
    hit_space = True
  if(hit_space):
    line = line[1:-1]
    line = tuple(line.split(','))
    parts.append(line)
  else:
    workflows.append(line)
parts.pop(0) #remove empty space
#print(parts)

converted_parts = list()
for part in parts:
    part_dict = {}
    for item in part:
        key, value = item.split('=')
        part_dict[key] = int(value)
    converted_parts.append(part_dict)
parts = converted_parts
#print(parts)

workflow_dict = dict()
for flow in workflows:
  values = flow.split('{')
  workflow_dict[values[0]] = values[1][:-1].split(',')
#print(workflow_dict)
ar = list()
### parts: listed as [{'a': 1222, 'x': 787, 's': 2876, 'm': 2655}, {'a': 2067, 'x': 1679, 's': 496, 'm': 44}]
### workflow_dict = workflow name: list of conditions
### partsdict = INDEX OF THE PART: current_workflow (in default)
### ar: whether each part got accepted or rejected

#everything starts at in
parts_dict = dict()
for i in range(len(parts)):
    parts_dict[i] = 'in'
#print(parts_dict)


#for each part 
for i in range(len(parts)):
  while(parts_dict[i] != 'A' or parts_dict[i] != 'R'):
    if(parts_dict[i] == 'A'):
      ar.append('A')
      break
    elif(parts_dict[i] == 'R'):
      ar.append('R')
      break
    conditions = workflow_dict[parts_dict[i]]
    for j in range(len(conditions)):
      if(':' in conditions[j]):
        values = conditions[j].split(':')
        letter = values[0][0]
        sign = values[0][1]
        number = values[0][2:]
        if(sign == '>'):
          if(int(parts[i][letter]) > int(number)):
            parts_dict[i] = values[1]
            break
          else:
            continue
        elif(sign == '<'):
          if(int(parts[i][letter]) < int(number)):
            parts_dict[i] = values[1]
            break
          else:
            continue
      else:
        #no ":" just set it
        parts_dict[i] = conditions[j]
        break
p1 = 0
p2 = 0
for i in range(len(ar)):
  if(ar[i] == 'A'):
    p2+=1
    part = parts[i]
    p1 += sum(part.values())
    

print(p1)


#part 2: use of permutations...cannot loop (see hyperneutrino)

with open('input19.txt') as file:
    block1, _ = file.read().split("\n\n")
  
workflows = {}

for line in block1.splitlines():
    name, rest = line[:-1].split("{")
    rules = rest.split(",")
    workflows[name] = ([], rules.pop())
    for rule in rules:
        comparison, target = rule.split(":")
        key = comparison[0]
        cmp = comparison[1]
        n = int(comparison[2:])
        workflows[name][0].append((key, cmp, n, target))

def count(ranges, name = "in"):
    if name == "R":
        return 0
    if name == "A":
        product = 1
        for lo, hi in ranges.values():
            product *= hi - lo + 1
        return product
    
    rules, fallback = workflows[name]

    total = 0

    for key, cmp, n, target in rules:
        lo, hi = ranges[key]
        if cmp == "<":
            T = (lo, min(n - 1, hi))
            F = (max(n, lo), hi)
        else:
            T = (max(n + 1, lo), hi)
            F = (lo, min(n, hi))
        if T[0] <= T[1]:
            copy = dict(ranges)
            copy[key] = T
            total += count(copy, target)
        if F[0] <= F[1]:
            ranges = dict(ranges)
            ranges[key] = F
        else:
            break
    else:
        total += count(ranges, fallback)
            
    return total

print(count({key: (1, 4000) for key in "xmas"}))