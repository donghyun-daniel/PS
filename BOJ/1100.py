cnt=0
for i in range(8):
    cnt+=input()[i%2::2].count('F')
print(cnt)