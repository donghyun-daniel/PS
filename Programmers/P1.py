import re

def solution(code, day, data):
    ans =[]
    d = []
    for i in data:
        l = re.split(r"price=|code=|time=", i)[1:]
        l = [i.rstrip() for i in l]
        if l[1] == code and l[2][:8] == day:
            d.append(l)
    d = sorted(d, key = lambda x : x[2])
    ans = [int(i[0]) for i in d]
    return ans

code = "012345"
day = "20190620"
data = ["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"]
print(solution(code, day, data))