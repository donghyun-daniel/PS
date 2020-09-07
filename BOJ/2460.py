now=0
ans=0
for i in range(10):
    off, on = map(int,input().split())
    now=max(now-off, 0)
    now+=on
    ans=max(ans, now)
print(ans)