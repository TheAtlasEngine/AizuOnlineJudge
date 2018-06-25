def quickSort(array):
    if len(array) in (0, 1):
        return array

    p = array[-1]
    left = [x for x in array[:-1] if x <= p]
    right = [x for x in array[:-1] if x > p]

    return quickSort(left) + [p] + quickSort(right)


def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-1, i, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    
    return array


n = int(input())
cards = []

for _ in range(n):
    card = input().split()
    card[0], card[1] = card[1], card[0]
    cards.append(card)

cardsBuff = cards[:]

quickSorted = quickSort(cards)
bubbleSorted = bubbleSort(cardsBuff)

if quickSorted == bubbleSorted:
    print("Stable")
else:
    print("Not stable")

print("QuickSort")
for card in quickSorted:
    card[0], card[1] = card[1], card[0]
    print(*card)

print("BubbleSort")
for card in bubbleSorted:
    print(*card)
