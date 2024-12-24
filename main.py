# 1 misol
from multiprocessing import Process
import time
#
# numbers = [1, 2, 3, 4, 5]
# def hisoblovchi(a):
#     s = 0
#     i = 0
#
#     while i < len(a):
#         s += a[i]
#         i += 1
#         print(s)
#         time.sleep(1)
# if __name__=="__main__":
#     th = Process(target=hisoblovchi,args=(numbers,))
#     th.start()
#     th.join()

#
# 2 misol
numbers = [1, 2, 3, 4]
# import random
# def alamshtiruvchi(a):
#     s = []
#     i = 0
#     while i < len(a):
#         sh = a[:]
#         random.shuffle(sh)
#         s.append(a)
#         print(sh)
#         i+=1
#         print("ishlayabdi!!!")
#         time.sleep(1)
# if __name__=="__main__":
#     th = Process(target=alamshtiruvchi,args=(numbers,))
#     th.start()
#     th.join()

# 3 misol
# numbers = [1, 2, 3, 4, 5]
# def hisoblovchi(a):
#     print("ishlayabdi!!!")
#     time.sleep(1)
#     print("eng katta son --->",max(a))
#     print("eng kichik son --->",min(a))
#
# if __name__=="__main__":
#     th = Process(target=hisoblovchi,args=(numbers,))
#     th.start()
#     th.join()

# 4 misol
# numbers = []
# def hisoblovchi(a):
#     if a:
#         print("Element bor")
#     else:
#         print("Elment yuq")
#     time.sleep(1)
# if __name__=="__main__":
#     th = Process(target=hisoblovchi,args=(numbers,))
#     th.start()
#     th.join()
# #

#5 misol
# numbers = [1, 1, 2, 3, 3, 4, 5, 5, 6, 7]
# def ochiruvchi(a):
#     c = []
#     for i in a:
#         if i not in c:
#             c.append(i)
#             print("ishlayabdi!!!")
#             time.sleep(1)
#     print(c)
#
# if __name__ == "__main__":
#     th = Process(target=ochiruvchi, args=(numbers,))
#     th.start()
#     th.join()

#  6 misol
# numbers = ["olma", "nok", "banan", "o'rik", "shaftoli", "ananas"]
# def ochiruvchi(a):
#     c = []
#     for i in a:
#         time.sleep(1)
#         print(i[::-1])
#
# if __name__ == "__main__":
#     th = Process(target=ochiruvchi, args=(numbers,))
#     th.start()
#     th.join()


# 7 misol
# numbers = ["olma", "nok", "banan", "o'rik", "shaftoli", "ananas"]
#
# def min_max(royxat: list):
#     max_word = max(royxat, key=len)
#     min_word = min(royxat, key=len)
#     print(f"eng kop so'zli element: {max_word}, eng kam so'zli element: {min_word}")
#     time.sleep(1)
#
# if __name__ == "__main__":
#     th = Process(target=min_max, args=(numbers,))
#     th.start()
#     th.join()
#

#
#8 misol
# from collections import Counter
# a = {"a": "olma","b": "olma","c": "nok","d": "banan","e":"nok" }
#
# def ochiruvchi(dict):
#     qiymat = dict.values()
#     h = Counter(qiymat)
#     t = []
#
#     for k, v in h.items():
#         if v > 1:
#             t.append(k)
#     print(t)
# if __name__ == "__main__":
#     th = Process(target=ochiruvchi, args=(a,))
#     th.start()
#     th.join()
#
#
#
#  9 misol
# # a = {"a": "1", "b": "olma", "c": "2", "d": "banan", "e": "nok"}
# def raqamlar(lugat):
#     num = []
#     for qiymat in lugat.values():
#         if qiymat.isdigit():
#             num.append(qiymat)
#     print(num)
#
# if __name__ == "__main__":
#     th = Process(target=raqamlar, args=(a,))
#     th.start()
#     th.join()
# #
# #

# 10 misol
# a = {"a": "1", "b": "olma", "c": "2", "d": "5", "e": "nok"}
# def numbers(lugat):
#     raqamlar = []
#     for qiymat in lugat.values():
#         if qiymat.isdigit():
#             raqamlar.append(int(qiymat))
#     for i in raqamlar:
#         time.sleep(1)
#         print(i**2)
#
# if __name__ == "__main__":
#     th = Process(target=numbers, args=(a,))
#     th.start()
#     th.join()
#


#  11 misol
# a = {"a": "1", "b": "olma", "c": "2", "d": "banan", "e": "nok"}
# def qiymat(lugat):
#     raqam = {}
#     for k, v in lugat.items():
#         if v.isdigit():
#             raqam[k] = int(v)
#     if not raqam:
#         return None
#     max_qiymat = max(raqam, key=raqam.get)
#     print("Eng katta qiymat",max_qiymat)
#
#
# if __name__ == "__main__":
#     th = Process(target=qiymat, args=(a,))
#     th.start()
#     th.join()


#  12 misol
# a = {"a": "1", "b": "olma", "c": "2", "d": "4", "e": "nok"}
# def ortacha_qiymat(lugat):
#     raqamli_qiymatlar = []
#     for qiymat in lugat.values():
#         if qiymat.isdigit():
#             raqamli_qiymatlar.append(int(qiymat))
#     if not raqamli_qiymatlar:
#         return None
#     ortacha = sum(raqamli_qiymatlar) / len(raqamli_qiymatlar)
#     print("prtacha qiymat",ortacha)
# if __name__ == "__main__":
#     th = Process(target=ortacha_qiymat, args=(a,))
#     th.start()
#     th.join()
#

# 13 misol
# a={'a': -10, 'b': -5, 'c': -100, 'd': -3, 'e': 0}
# b={'a': 10, 'b': 42, 'c': 3.14, 'd': -5, 'e': 100}
#
# def qoshuvchi(d1: dict, d2: dict):
#     merged = d1.copy()
#     for key, value in d2.items():
#         if key in merged:
#             merged[key] += value
#         else:
#             merged[key] = value
#     print(merged)
# if __name__ == "__main__":
#     pr1 = Process(target=qoshuvchi, args=(a, b,))
#     pr1.start()
#     pr1.join()

# 14 misol
# a = {"a": 10, "b": 42, "c": 3.14, "short": -5, "verylongkey": 100}
# def eng_uzun_va_qisqa_kalit(lugat):
#     kalitlar = list(lugat.keys())
#     eng_qisqa = min(kalitlar, key=len)
#     eng_uzun = max(kalitlar, key=len)
#
#     print(f"eng qizqa kalit {eng_qisqa},eng uzun kalit {eng_uzun}")
# if __name__ == "__main__":
#     pr1 = Process(target=eng_uzun_va_qisqa_kalit, args=(a,))
#     pr1.start()
#     pr1.join()


#  15 misol
# a = {"a": "1", "b": "olma", "c": "2", "d": "4", "e": "nok"}
#
# def nums(d: dict):
#     for key, value in d.items():
#         if isinstance(value, str) and value.replace('.', '', 1).isdigit():
#             d[key] = float(value) if '.' in value else int(value)
#     print(d)
# if __name__ == "__main__":
#     pr1 = Process(target=nums, args=(a, ))
#     pr1.start()
#     pr1.join()


#  16  misol
# a = {"a": "1", "b": "olma", "c": "2", "d": "4", "e": "nok"}
#
# def kopaytiruvchi(d: dict):
#     new_dict = {}
#     for key, value in d.items():
#         time.sleep(0.1)
#         if isinstance(value, (int, float)):
#             new_dict[key] = value * 2
#         else:
#             new_dict[key] = value
#     print(new_dict)
#
# if __name__ == "__main__":
#     pr1 = Process(target=kopaytiruvchi, args=(a, ))
#     pr1.start()
#     pr1.join()


 # 17 misol
# a = {"a": "olma","b": "olma","c": "nok","d": "banan","e":"nok" }
# def ab(d: dict):
#     for key, value in d.items():
#         if isinstance(value, str):
#             d[key] = value[::-1]
#     print(d)
# if __name__ == "__main__":
#     pr1 = Process(target=ab, args=(a, ))
#     pr1.start()
#     pr1.join()