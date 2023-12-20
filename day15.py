
with open('input15.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]
line = lines[0]
words = line.split(',') #all the strings


def HASH(word):
  current_value = 0
  for char in word:
    current_value += ord(char)
    current_value *= 17
    current_value %= 256
  return current_value

def part_1():
  p1 = 0
  for word in words:
    p1 += HASH(word)
  return p1

boxes = [[] for i in range(256)]
positions = dict() #sequence value: {box number, lense number} 

def part_2():
  p2 = 0
  for word in words:
    if('=' in word and word.split('=')[0] not in positions):
      #completely new sequence: add to a box, create new part in dict
      values = word.split("=") #values[0] is the sequence, values[1] = lens
      boxes[HASH(values[0])].append(values[0])
      positions[values[0]] = [HASH(values[0]), int(values[1])]
    elif('=' in word and word.split('=')[0] in positions):
      #sequence exists in a box: only update the dict (lens)
      values = word.split("=") #values[0] is the sequence, values[1] = lens
      positions[values[0]] = [HASH(values[0]), int(values[1])]
    elif('-' in word):
      #-
      sequence = word[0:-1] #everytrhing but the -
      if(sequence in positions):
        #REMOVE IT FROM DICT AND BOX 
        del positions[sequence]
        boxes[HASH(sequence)].remove(sequence)
    
    
  #calculate all the focusing powers
  for key in positions:
    box_number = positions[key][0] + 1
    slot_position = boxes[HASH(key)].index(key) + 1
    lens = positions[key][1]
    power = box_number * slot_position * lens
    p2 += power 
  return p2  
    
print(part_1())
print(part_2())


