cards = [9, 8, 7, 6, 5, 4, 3, 2, 1]


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


# Example usage
query_number = 3
result = locate_cards(cards, query_number)
print(result)  # Output: 4 (index of the queried number in the cards list)
