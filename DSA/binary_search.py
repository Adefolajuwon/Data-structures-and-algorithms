

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


test = []
# ok
test.append({
    'input': {
        'cards': [10, 9, 8, 7, 6, 5, 4, 3, 2, 2, 1],
        'query': 10},
    'output': 0
})
test.append({
    'input': {
        'cards': [8, 7, 6, 5, 4, 3, 2, 1],
        'query': 8
    },
    'output': 0
})
evaluate_test_case(locate_card, test[0])

# leetcode


def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid - 1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)


def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        elif nums[mid] > target:
            return 'left'
    return binary_search(0, len(nums)-1, condition)


def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return first_and_last_position(nums, target)
# end


# rotated list
# nums = [6, 7, 8, 2, 3, 4, 5]


# def binary_search(nums):
#     lo = 0
#     hi = len(nums)-1
#     mid = (lo + hi) // 2
#     mid_number = nums[mid]
#     position = 1
#     while position <= len(nums):
#         if mid > 0 and mid_number < h1:
#             r
