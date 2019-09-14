# class point:
#     def __init__ (self,name,x,y):
#         self.name = name
#         self.cor = (x,y)

# A = point("A",10,30)
# B = point("B",10,10)


# PIGU = {A:('A','B'), B:'B'}
    

# for node in PIGU:
#     print(node.cor[0])


# s = "abc deb hhh"
# print(s[0:s.index(' ')])

from dij_cmu import *
path = findPath('WEH 6330', 'GHC 5730')
print(path)