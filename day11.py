#grids are killing me.. thanks hyper neutrino (CREDIT)
grid = open('input11.txt').read().splitlines()
#print(grid)

empty_rows = [r for r, row in enumerate(grid) if all(ch == '.' for ch in row)] #this is just an empty row
empty_cols = [c for c, col in enumerate(zip(*grid)) if all(ch == '.' for ch in col) ]

points = [(r,c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == '#'] # all galaxies

total = 0

for i, (r1,c1) in enumerate(points):
  #go thru each pair of points index, point
  for (r2,c2) in points[:i]:
    #go to points up to i (don't double count, dont repeat i) compare the galaxies
    for r in range(min(r1,r2), max(r1,r2)):
      total += 2 if r in empty_rows else 1 #galaxy expansion
    for c in range(min(c1,c2), max(c1,c2)):
      total += 2 if c in empty_cols else 1
print(total)

#for part two, the expansion is just 1000000 so replace += 2 with 1 million
