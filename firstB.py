data = {'1': ['a', 'b'],
        '2': ['c', 'd'],
        '3': ['e', 'f']}
for i in data['1']:
    for j in data['2']:
        for k in data['3']:
            print(i + j + k)
