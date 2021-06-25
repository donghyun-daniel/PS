def conv(t):
    h, m = t.split(":")
    return int(h)*60 + int(m)

def solution(n, t, m, timetable):
    timetable = sorted(list(map(conv, timetable)))
    timetable = [t for t in timetable if t <= 540 + (n-1) * t]
    now = 540
    cap = 0
    idx = 0
    last = 0
    while n and idx < len(timetable):
        if timetable[idx] <= now:
            last = timetable[idx]
            idx += 1
            cap += 1
        else:
            now += t
            cap = 0
        if cap == m:
            now += t
            n -= 1
            cap = 0
    
    ans = 0
    return ans

n = 1
t = 1
m = 5
timetable = ["09:10", "09:09", "08:00"]
print(solution(n, t, m, timetable))