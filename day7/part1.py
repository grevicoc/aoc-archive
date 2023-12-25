import math

FIVE_OF_A_KIND = 10
FOUR_OF_A_KIND = 9
FULL_HOUSE = 8
THREE_OF_A_KIND = 7
TWO_PAIR = 6
ONE_PAIR = 5
HIGH_CARD = 4

mapCardVals = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}

class Card:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.level = 0

        mapCard = {}
        for card in cards:
            if card in mapCard:
                mapCard[card] += 1
            else:
                mapCard[card] = 1
        
        if len(mapCard.keys()) == 1:
            self.level = FIVE_OF_A_KIND
        elif len(mapCard.keys()) == 2:
            if 4 in mapCard.values():
                self.level = FOUR_OF_A_KIND
            else:
                self.level = FULL_HOUSE
        elif len(mapCard.keys()) == 3:
            if 2 in mapCard.values():
                self.level = TWO_PAIR
            else:
                self.level = THREE_OF_A_KIND
        elif len(mapCard.keys()) == 4:
            self.level = ONE_PAIR
        else:
            self.level = HIGH_CARD
    
    def compareTo(self, card):
        # print(self)
        # print(card)
        if self.level > card.level:
            return 1
        
        if self.level < card.level:
            return -1
        
        for i in range (5):
            if mapCardVals[self.cards[i]] > mapCardVals[card.cards[i]]:
                return 1
            elif mapCardVals[self.cards[i]] < mapCardVals[card.cards[i]]:
                return -1
            else:
                continue
    
    def __str__(self) -> str:
        return f"CARDS: {self.cards} | LEVEL: {self.level}"


# [2, 19, 40, 50, 100]
# l 3
# r 4
# m 3

class PrioQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, card: Card):
        left = 0
        right = len(self.queue)-1
        mid = math.floor((right+left)/2)

        while right >= left:
            if self.queue[mid].compareTo(card) == 1:
                right = mid-1
                mid = math.floor((right+left)/2)
                continue

            if self.queue[mid].compareTo(card) == -1:
                left = mid+1
                mid = math.floor((right+left)/2)
        
        self.queue.insert(left, card)
    
    def __str__(self) -> str:
       return f"{self.queue}"
            
queue = PrioQueue()
file = open("input.txt", "r")
for line in file.readlines():
    input = line.strip().split(" ")
    card = Card(input[0], input[1])
    queue.enqueue(card)

sum = 0
i = 1
for card in queue.queue:
    print(card)
    sum += int(card.bid) * i
    i += 1

print(sum) # your answer is too low