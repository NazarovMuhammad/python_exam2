def fanc(a, b):
    return a.intersection(b)

a = input().split()
b = input().split()
set1 = set(a)
set2 = set(b)


print(fanc(set1,set2))