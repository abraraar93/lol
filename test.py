# # print(int(0b100001))
# # print(bin(30))
# # print(0b00111)
# # print(25 ^ 30)
#
# list = [1, 3, 'asset', 45, {1: 'happy', "lol": 1}]
# import math
#
# # list.clear()
# # B = list.copy()
# B = [4, 5, 6, 9]
# # B.extend(list)
# # print(B.index(4))
# print(int(math.sqrt(4)))
# print(B.sort(reverse=True))
# print(sorted(B))
# B.append({'lol': 678})
# for i in B:
#     print(i)

list = input('enter a list of name').replace(' ' , '')

def checkIfnameGreaterThan5(lst):
    a = lst.split(',')
    print(a)
    b = 0
    for i in a :
        if len(i) > 5:
            b += 1
        else:
            pass
    return b
    print(b)

print(checkIfnameGreaterThan5(list))
