#thank you hyper neutrino again!
letter_map = {"T": "A", "J":".", "Q": "C", "K":"D", "A":"E"} #a thru e strength
#FOR PART 1, J SHOULD BE 'B'
def classify(hand):
  # is it a five, four, pair, etc
  counts = [hand.count(card) for card in hand] #get the count of each hand 
  if 5 in counts:
    return 6
  if 4 in counts:
    return 5
  if 3 in counts:
    if 2 in counts:
      return 4
    return 3
  if counts.count(2) == 4:
    #pair
    return 2
  if 2 in counts:
    return 1
    #1 pair
  return 0 #high

def replacements(hand):
  if hand == '':
    return ['']
  return [x + y 
          for x in ("23456789TQKA" if hand[0] == 'J' else hand[0]) 
          for y in replacements(hand[1:])]

def classify2(hand):
  return max(map(classify, replacements(hand)))

def strength(hand):
  #use classify2 for part 2
  return (classify2(hand), [letter_map.get(char, char) for char in hand])

cards = list()
for line in open('input7.txt'):
  hand, bid = line.split()
  cards.append((hand, int(bid))) #bid as a number and not a string

cards.sort(key = lambda play: strength(play[0])) #strength of each card

total = 0
for rank, (hand, bid) in enumerate(cards, 1):
  total += rank * bid
print(total)