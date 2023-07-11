# 18을 이진수로 변환

n=18

result=' '
while n > 0:
    result = str(n % 2) + result
    n //=2

print(result)