

from jovian.pythondsa import evaluate_test_case


def locate_card(cards, query):
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


test = {
    'input': {
        'cards': [10, 9, 8, 7, 6, 5, 4, 3, 2, 2, 1],
        'query': 5
    },
    'output': 5
}

evaluate_test_case(locate_card, test)
