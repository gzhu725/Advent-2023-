import sympy
#credit to stack overflow for this function
def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return None
    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

def sign(a):
  if a < 0:
    return -1
  elif a == 0:
    return 0
  else:
    return 1

output = list()
#formatting
for line in open("input24.txt", "r").read().strip().split('\n'):
    p,v = line.split(' @ ')
    cur_p = [int(i) for i in p.split(',')]
    cur_v = [int(i) for i in v.split(',')]
    output.append((cur_p,cur_v))

coordinates = [] #we are adding point1, point2 in order
for value in output:
  hail_coord = list()
  hail_coord.append(value[0][0])
  hail_coord.append(value[0][1])
  hail_coord = tuple(hail_coord)
  next_coord = tuple([hail_coord[0] + value[1][0], hail_coord[1] + value[1][1]])
  coordinates.append(list(((hail_coord), (next_coord))))
#print(coordinates) #each line listed as two points 
#part 1 here 
in_range = 0
for i in range(len(coordinates)):
  for j in range(i+1, len(coordinates)):
    intersection = line_intersection(coordinates[i], coordinates[j])
    if intersection != None:
      #there is some sort of intersection, but you want to check if they already crossed + in bounds
      #from jackpal github
      def crossed_future(sect, a):
        intersect_x, intersect_y = intersection
        return sign(intersect_x - a[0][0]) == sign(a[1][0]) and sign(intersect_y - a[0][1]) == sign(a[1][1])
      if crossed_future(intersection, output[i]) and crossed_future(intersection,output[j]):
        #they have crossed, then we check whether the intersection is in range
        intersect_x, intersect_y = intersection
        if(200000000000000 <= intersect_x <= 400000000000000 and 200000000000000 <= intersect_y <= 400000000000000):
          in_range+=1
#prints part 1 answer
print(in_range)



#part 2:basically solving all the equations with one solution. use sympy library - hyperneutrinos math lol 
xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")
hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in open('input24.txt')]
equations = []


for i, (sx, sy, sz, vx, vy, vz) in enumerate(hailstones):
    equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr)) #all the equations
    equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
    if i < 2:
        continue
    answers = [soln for soln in sympy.solve(equations) if all(x % 1 == 0 for x in soln.values())]
    if len(answers) == 1:
      #just need one answer
        break
    
answer = answers[0]
#part 2
print(answer[xr] + answer[yr] + answer[zr])