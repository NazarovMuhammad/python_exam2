def func(a):
    if a == a[::-1]:
      return "True"
    else:
        return "False"


a = input()#"abccba"
print(func(a)) 