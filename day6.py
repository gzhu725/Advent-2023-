
'''with open('input6.txt') as reader:
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
  for j in range(1, (time + 1)/2):
    if((j * (time-j)) in possible_distances_traveled):
      break
    else:
      possible_distances_traveled.append(j*(time-j))
  count = 2 * len(list(filter(lambda x: x > distance, possible_distances_traveled)))
  if(time % 2 == 0):
    count +=1
  ways.append(count)

print(ways)
p1 = 1
for value in ways:
  p1 *= value
print(p1)
'''



#over complicated the problem above, ^^^^ much more efficeint down here
time =  54946592
distance = 302147610291404
def f(time, distance):
  ans = 0
  for x in range(time+1):
    dist = x*(time-x)
    if dist>distance:
      ans += 1
  return ans


print(f(time,distance))