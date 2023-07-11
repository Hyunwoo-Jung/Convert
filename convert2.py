n=18

def convert(n, base):
    result = ' '
    while n>0:
        result = str(n % base) + result
        n //= base
    return result

print(convert(n, 2)) # 2진법으로 변환
print(convert(n, 3)) # 3진법으로 변환
print(convert(n, 8)) # 8진법으로 변환