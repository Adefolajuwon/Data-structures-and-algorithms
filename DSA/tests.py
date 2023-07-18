tests = []
# query is th first element
tests.append({
    'inputs': {
        'cards': [10, 9, 8, 7, 6, 5, 4, 3, 2, 2, 1],
        'query': [5]
    },
    'output': 5
},
)

# query is in the midlle
tests.append({
    'inputs': {
        'cards': [6, 5, 4, 3, 2, 1],
        'query': 3
    },
    'output': 3
})
# nums = [5,7,7,8,8,10]
# target = 7
# # def first_index():
# #     lo = 0
# #     hi = lens(nums) - 1
# #     mid = (lo + hi) // 2
# #     middle_number = nums[mid]
# #     while lo <= hi
# #       if mid_number = query
# #        return mid_number
# #      elif target < 3


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
