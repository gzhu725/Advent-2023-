import ctypes
#mutable string time
mutable_grid = list()
for line in open('input14.txt').read().split():
  mutable = ctypes.create_unicode_buffer(line)
  mutable_grid.append(mutable)

rock_indexes = list() #keep track of the original indexes of the rocks (row, col)

for i in range(len(mutable_grid)):
  for j in range(len(mutable_grid[i])):
    if(mutable_grid[i][j] == 'O'):
      rock_indexes.append([i,j])

def part1():
  for number, indexes in enumerate(rock_indexes):
    original_index = indexes #1,0
    row_index = original_index[0] #
    while(row_index > 0 and mutable_grid[row_index - 1][original_index[1]] == '.'):
      row_index -= 1
    mutable_grid[row_index][original_index[1]] = 'O'
    if(row_index != original_index[0]):
      mutable_grid[original_index[0]][original_index[1]] = '.'
    
  for i in range(len(mutable_grid)):
    mutable_grid[i] = mutable_grid[i].value
    
  p1 = 0
  for i in range(len(mutable_grid)):
    rock_count = mutable_grid[i].count('O')
    load = rock_count * (len(mutable_grid) - i)
    p1 += load
  print(p1) 



#part 2 below, needed hyper neutrino since brute force is not going to be efficient enough 
grid = tuple(open('input14.txt').read().splitlines())

def cycle():
    global grid
    for _ in range(4):
        grid = tuple(map("".join, zip(*grid)))
        grid = tuple("#".join(["".join(sorted(tuple(group), reverse=True)) for group in row.split("#")]) for row in grid)
        grid = tuple(row[::-1] for row in grid)

seen = {grid}
array = [grid]

iter = 0

while True:
    iter += 1
    cycle()
    if grid in seen:
        break
    seen.add(grid)
    array.append(grid)
    
first = array.index(grid)
    
grid = array[(1000000000 - first) % (iter - first) + first]

print(sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))