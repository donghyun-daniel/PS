s=[input() for i in range(5)]
max_len = max([len(i) for i in s])
for idx in range(max_len):
    for i in range(5):
        if idx < len(s[i]):
            print(s[i][idx], end = '')