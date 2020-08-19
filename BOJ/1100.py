cnt=0
for i in range(8):
    if i%2==0:
        cnt+=input()[::2].count('F')
    else:
        cnt+=input()[1::2].count('F')
print(cnt)