#needed hyper neutrinos help on this one --> figuring out area based on path! grid problem :( 

points = [(0,0)] 
#each direction is one unit move based on the directory
dirs = {
  "U": (-1,0),
  "D": (1,0),
  "L":(0,-1),
  "R": (0,1)
}

b = 0
for line in open('input18.txt'):
  direction, steps, color = line.split() #R 6 hexcolor
  #for part two, direction and step are based on the color (part 2 code rechanges the value of color and direction)
  color = color[2:-1]
  if(color[-1] == '0'):
    direction = 'R'
  elif(color[-1] == '1'):
    direction = 'D'
  elif(color[-1] == '2'):
    direction = 'L'
  else:
    direction = 'U'
  steps = int(color[0:-1], 16) 
  dr, dc = dirs[direction]
  steps = int(steps)
  b += steps
  r, c = points[-1] #most recent point that we have
  points.append((r + dr * steps, c + dc *steps)) #move to the next appropriate point 
#print(points)
area = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2
i = area - b // 2 + 1
print(i+b) #part 1

#part 2 : solved on my own (just changing the points based on color)