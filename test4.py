'''题目：输入三个整数x,y,z，请把这三个数由小到大输出。

程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，
如果x>z则将x与z的值进行交换，这样能使x最小。'''

import timeit
from pyecharts.charts import Line
# lst = [33,3,334,6]

# def merge_sort(num):
#     if len(num) <=1:
#         return num
#     mid = len(num) // 2
#     left_lst = merge_sort(num[:mid])
#     right_lst = merge_sort(num[mid:])
#     return merge(left_lst,right_lst)

# def merge(left,right):
#     result =[]
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i +=1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result

# print(merge_sort(lst))

# def fibonacci(n):
#     if n <=1 :
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n -2)
    
# print(fibonacci(5))
        
    
def calc_monthly_growht(current_month,previous_month):
    if previous_month == 0:
        raise ValueError("Previous month's value cannot be zero to avoid division by zero.")
    growht = ((current_month - previous_month) / previous_month) * 100
    return growht

# def test():
#     test_case = [
#         (100,50),
#         (129,39)

#     ]
#     for current_month,previous_month in test_case:
#         result = calc_monthly_growht(current_month,previous_month)
#         print(result)

# test()


data_lst = [12,22,34,65,45,63,78,87,88,98,109]
# print(len(data_lst))
# for i in range(len(data_lst)):
#     if i+2 <= len(data_lst):
#         result = data_lst[i:i+2]
        

#         print(f'同比上月的增加率为：{round(calc_monthly_growht(result[1],result[0]),2)}.%,净利润为 {result[1] - result[0]} 万元。')

x_data = list(range(len(data_lst)))
y_data = data_lst

line = (Line().add_xaxis(x_data).add_yaxis('增长率',data_lst))
line.render('rowth.html')


def perv(cur,rowth):
    if cur == 0:
        print('error data,this cur no zero')
    per = cur / (1 + rowth /100)
    return per

print(round(perv(98,11.36),2))