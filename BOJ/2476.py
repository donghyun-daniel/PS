score = []
for i in range(int(input())):
    dice = list(map(int, input().split()))
    if dice.count(dice[0]) == 3:
        score.append(10000 + dice[0] * 1000)
    elif dice.count(dice[0]) == 2:
        score.append(1000 + dice[0] * 100)
    elif dice.count(dice[1]) == 2:
        score.append(1000 + dice[1] * 100)
    else:
        score.append(max(dice) * 100)
print(max(score))