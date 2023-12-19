
with open('input6.txt') as reader:
  lines = [line.strip('') for line in reader.readlines()]

input_data = []
for line in lines:
  line = line.split()
  input_data.append(line)

ways = list()
for i in range(1,len(input_data[0])):
  time = int(input_data[0][i])
  distance = int(input_data[1][i])
  possible_distances_traveled = list()
  for j in range(1, time + 1):
      possible_distances_traveled.append(j*(time-j))
  count = len(list(filter(lambda x: x > distance, possible_distances_traveled)))
  ways.append(count)
  
  #print(possible_distances_traveled)
print(ways)
p1 = 1
for value in ways:
  p1 *= value
print(p1)

