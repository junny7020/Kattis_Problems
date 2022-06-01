data = input().split()
numberOfHands = int(data[0])
dominantSuit = data[1]

def dom_val(x):
    return {
        'A': 11,
        'K': 4,
        'Q': 3,
        'J': 20,
        'T': 10,
        '9': 14,
        '8': 0,
        '7': 0,
    }[x]

def non_dom_val(x):
    return {
        'A': 11,
        'K': 4,
        'Q': 3,
        'J': 2,
        'T': 10,
        '9': 0,
        '8': 0,
        '7': 0,
    }[x]

totalValue = 0
for _ in range(numberOfHands):
    for _ in range(4):
        card = input()
        value = card[0]
        suit = card[1]

        if suit == dominantSuit:
            totalValue += dom_val(value)
        else:
            totalValue += non_dom_val(value)

print(totalValue)