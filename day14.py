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

part1()