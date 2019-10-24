# -*- utf-8 -*-
import pickle
# def f(p):
#     print (p)
#
# a = f
#
# with open('tmp.pk', 'wb') as file:
#     pickle.dump(a, file)
# # print(b)

with open('tmp.pk', 'rb') as file:
    f = pickle.load(file)
    print(f)