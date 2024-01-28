# # # # # n = int(input())
# # # # # c = list(map(int, input().split(" ")))
# # # # # listish = []
# # # # # summa = -2
# # # # # for i in c:
# # # # #     summa += 1
# # # # # count = 0
# # # # # i = 0
# # # # # while summa != i:
# # # # #     if c[i] != c[i+1]:
# # # # #         count += 1
# # # # #         i += 1
# # # # #     i += 1
# # # # # print(count)
# # # # a = list(map(int, input().split(" ")))
# # # # listish = []
# # # # for b in range(a[0]):
# # # #     for c in range(a[0]):
# # # #         if b <= a[1] and c <= a[1] and b*c == a[0]:
# # # #             listish.append(b)
# # # #             listish.append(c)
# # # #         else:
# # # #             for d in range(a[0]):
# # # #                 if b <= a[1] and c <= a[1] and d <= a[1] and b*c*d == a[0]:
# # # #                     listish.append(b)
# # # #                     listish.append(c)
# # # #                     listish.append(d)
# # # # listish = set(listish)
# # # # listish_1 = []
# # # # summa = 0
# # # # for i in listish:
# # # #     if i != 1:
# # # #         listish_1.append(str(i))
# # # #         summa += 1
# # # # listish_1 = reversed(listish_1)
# # # # if a[0]%a[1]==0:
# # # #     print(summa)
# # # #     print(" ".join(listish_1))
# # # # else:
# # # #     print(-1)
# # # n = 6
# # # c = [1, 3, 1, 5, 3, 5]
# # # for a in c:
# # #     for b in c:
# # #         if 
# # # print()
# # # import math
# # # def calculate_vectors(x1, y1, x2, y2, x3, y3, x4, y4):
# # #     len_a, len_b = math.sqrt((x2 - x1)**2 + (y2 - y1)**2), math.sqrt((x4 - x3)**2 + (y4 - y3)**2)
# # #     sum_vector1, sum_vector2 = (x2 - x1) + (x4 - x3), (y2 - y1) + (y4 - y3)
# # #     scalar_product, vector_product = (x2 - x1) * (x4 - x3) + (y2 - y1) * (y4 - y3), (x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3)
# # #     area_triangle = 0.5 * abs(vector_product)
# # #     print(round(len_a, 9), round(len_b, 9))
# # #     print(round(sum_vector1, 9), (round(sum_vector2, 9)))
# # #     print(round(scalar_product, 9), round(vector_product, 9))
# # #     print(round(area_triangle, 9))
# # # a = list(map(float, input().split()))
# # # b = list(map(float, input().split()))
# # # x1, y1, x2, y2 = a
# # # x3, y3, x4, y4 = b
# # # res = calculate_vectors(x1, y1, x2, y2, x3, y3, x4, y4)

# # def quorter(x, y):
# #     if x > 0 and y > 0:
# #         return 1
# #     elif x < 0 and y > 0:
# #         return 2
# #     elif x < 0 and y < 0:
# #         return 3
# #     elif x > 0 and y < 0:
# #         return 4
# #     else:
# #         return 0
# # x, y = map(float, input().split())
# # print(quorter(x, y))

 
# n = int(input().strip())
# points = []
# for _ in range(n):
#     x, y = map(int, input().split())
#     points.append([x, y])
# Q1 = Q2 = Q3 = Q4 = AXIS = 0
# for x, y in points:
#     if x == 0 or y == 0:
#         AXIS += 1
#     elif x > 0 and y > 0:
#         Q1 += 1
#     elif x < 0 and y > 0:
#         Q2 += 1
#     elif x < 0 and y < 0:
#         Q3 += 1
#     elif x > 0 and y < 0:
#         Q4 += 1
# print(f"Q1: {Q1}")
# print(f"Q2: {Q2}")
# print(f"Q3: {Q3}")
# print(f"Q4: {Q4}")
# print(f"AXIS: {AXIS}")

x, y, a, b = map(int, input().split())
c = -a*x - b*y
print(a, b, c)