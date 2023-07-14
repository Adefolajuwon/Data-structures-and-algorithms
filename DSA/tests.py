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
