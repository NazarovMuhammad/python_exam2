def func(name,cnt = 1):
    for i  in name:
        if (i.isalpha()):
            cnt+=1
            return cnt
name = input()
print(func(name))