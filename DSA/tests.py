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
