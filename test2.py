arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
bonus = 0
profit = int(input())


for idx in range(6):
    if profit > arr[idx]:
        bonus += (profit - arr[idx])* rat[idx]
        print(bonus)
        profit = arr[idx]
        # break

