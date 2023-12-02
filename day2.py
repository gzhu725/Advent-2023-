
with open('input2.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

#lines = all lines of the input
#PART 1
quantity_dict = {
  "blue": 14,
  "red": 12,
  "green": 13
}
p1 = 0
for line in lines:
  words = line.split(' ')
  #every single word in the line
  game_no = int(words[1].strip(':'))
  is_valid_game = True
  for i in range(2, len(words) -1, 2):
    quantity = int(words[i]) #the number of cubes grabbed
    color = words[i+1].strip(",;") #the color of the cube
    if(quantity > quantity_dict[color]):
      #too many!!
      is_valid_game = False
  if(is_valid_game):
    p1 += game_no
#print(p1)

#part 2: find the max for each number 
blue_quant = list()
red_quant = list()
green_quant = list()
p2 = 0
for line in lines:
  words = line.split(' ')
  #every single word in the line
  game_no = int(words[1].strip(':'))
  for i in range(2, len(words) -1, 2):
    quantity = int(words[i]) #the number of cubes grabbed
    color = words[i+1].strip(",;") #the color of the cube
    if(color == "blue"):
      blue_quant.append(quantity)
    elif(color == "green"):
      green_quant.append(quantity)
    else:
      red_quant.append(quantity)
  power_set = max(red_quant) * max(green_quant) * max(blue_quant)
  p2 += power_set
  red_quant = [] #reset after finding the max for each game. 
  green_quant = []
  blue_quant = []
print(p2)



    
  
