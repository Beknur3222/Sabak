# #laba4-1
# t = str(input("Введите текст: "))
# n=0
# m=0
# for i in range(len(t)):
#     if t[i].isupper() == True:
#         n+=1
#     else:
#         m+=1
# if n>m:
#     print(t.upper())
# else:
#     print(t.lower())
#laba4-2
i = False
while i == True:
    a = str(input("A = "))
    b = str(input("B = "))
    if a.isdigit() == True and b.isdigit() == True:
        print("Sum =", a + b)
        i == True
    else:
        False