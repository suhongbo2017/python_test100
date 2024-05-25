import time

start = time.time()
lst = [[a,b,c] for a in range(5) for b in range(5) for c in range(5) if (a != b) and (a != c) and (b != c)]
end = time.time()


print(lst)


