def funcao():
    global n1
    n1 = 4
    print(f'N1 local vale {n1}')


n1 = 2
print(f'N1 global vale {n1}')
funcao()
print(f'N1 global vale {n1}')