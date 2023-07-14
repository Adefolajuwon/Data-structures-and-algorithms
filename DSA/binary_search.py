# cards = [9, 8, 7, 6, 5, 4, 3, 2, 1]


def locate_cards(cards, query):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]
        if mid_number == query:
            return mid
        elif mid_number > query:
            hi = mid - 1
        elif mid_number < query:
            lo = mid + 1
    return -1


cards = [1, 2, 3, 4, 5, 6, 7, 8, 9]
query = 10
result = locate_cards(cards, query)
print(result)
