k = (1,2,3,4,5,10,2.3,"string")
# nowa_lista =[]
# for x in k:
#     nowa_lista.append(x*2)
# print(nowa_lista)
def razy_dwa(elem):
    return elem * 2
print(list(map(razy_dwa, k)))

print(list(map(lambda x: x*2, k)))