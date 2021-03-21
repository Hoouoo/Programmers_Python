'''
Programmers - 주식 가격
Stack / Python3

date : 2021-03-22
'''

prices = [1,2,3,2,3]
answer = [0] * len(prices)
for i in range(0, len(prices)):
    for j in range(i+1, len(prices)):
        if prices[i] <= prices[j]:
            answer[i] += 1
        else:
            answer[i] += 1
            break
print(answer)