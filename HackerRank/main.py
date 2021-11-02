
ratings = [4, 2, 5, 1]

ratings.sort()

totalMin = 0
for i in range(0, len(ratings), 2):
    min = abs(ratings[i] - ratings[i+1])
    totalMin += min

print(totalMin)

