x,y,w,h=map(int,input().split())
w_min=min(x,w-x)
h_min=min(y,h-y)
print(min(w_min,h_min))