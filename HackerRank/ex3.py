scheduleStart = [6, 1, 2, 4]
scheduleEnd = [8, 9, 4, 7]

intervals = list()
presentation = list()

for i in range(0, len(scheduleStart)):
    presentation.clear()
    presentation.append(scheduleStart[i])
    presentation.append(scheduleEnd[i])
    intervals.append(presentation[:])

intervals.sort(key=lambda x:x[0])

maxPresentations = 0

for i in range(0, len(intervals) - 1):
    for j in range(i, len(intervals) - 1):
        if intervals[i][j] <= intervals[i][j + 1]:
            maxPresentations += 1



print(intervals)