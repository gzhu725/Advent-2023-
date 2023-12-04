
with open('input4.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]


#file formatting...
formatted_lines = []
for line in lines:
  line = line.split(" ")
  formatted_lines.append(line)

#p1: part 1 answer
#p2: part 2 answer 
p1 = 0
p2 = 0
card_copies = dict()
for card in formatted_lines:
  winning_numbers = []
  your_numbers = []
  is_half_way = False #see if we have seen the "|" symbol
  original_card_no = -1
  for i in range(len(card)):
    if(card[i] and card[i][-1] == ":"):
        original_card_no = int(card[i].strip(":"))
    if(card[i] == '|'):
      is_half_way = True
    if(card[i].isdigit() and not is_half_way):
      winning_numbers.append(int(card[i]))
    elif(card[i].isdigit() and is_half_way):
      your_numbers.append(int(card[i]))
  good_card_no = len(set(your_numbers).intersection(set(winning_numbers)))
  copies_gained = [i for i in range(original_card_no, original_card_no + good_card_no+1)]
  multiplier = 1
  if(copies_gained[0] in card_copies):
    multiplier = card_copies[copies_gained[0]]

  for value in copies_gained:
    if value not in card_copies:
      card_copies[value] = 1
    else:
      card_copies[value] += multiplier
  if(good_card_no > 0):
    p1 += 2 ** (good_card_no -1)
for value in card_copies:
  p2 += card_copies[value]
print(p2)
#print(p1)

#my solution for part 2 doesn't work but it works for the sample case
#^ issues? limitations in the dictionary or algorithmic fault? 
#usxd jonathan paulson's solution to find p2
  