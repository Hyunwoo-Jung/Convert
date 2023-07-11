# 2진수를 10진수로 변환

n ='10010'

result = 0

for i in range(len(n)):
    result += int(n[i]) * (2 ** (len(n) - i - 1))
# int(n[i] -> 한 문자씩 꺼내기
# (len(n) - i - 1) -> 제곱부분을 계산

print(result)