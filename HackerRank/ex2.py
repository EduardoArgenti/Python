from collections import defaultdict

arr = [7, 12, 3]

matrix = list()
unique = list()
current = list()

# Building the matrix
for i in arr:
    freq = 0
    current.clear()

    if i not in unique:
        unique.append(i)
        freq = arr.count(i)
        current.append(i)
        current.append(freq)
        matrix.append(current[:])
    else:
        continue

print('Original: ', end='')
print(matrix)

# Sort descending by frequency
matrix.sort(key=lambda x:x[1], reverse=True)
print('Ordenada 1: ', end='')
print(matrix)

# Sort ascending by value for matching frequencies
d = defaultdict(lambda: 0)
for i in range(len(arr)):
        d[arr[i]] += 1
matrix.sort(key=lambda x: (-d[x], x))

print('Ordenada 2: ', end='')
print(matrix)




