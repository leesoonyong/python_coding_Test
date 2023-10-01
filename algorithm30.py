# 백준 1978번
n = input()
numbers = map(int, input().split())  # 소수체크할값들
result = 0
for num in numbers:
    check = 0
    if num > 1:  # 1은 소수가아니기 때문에 1보다 클 경우만 체크
        for i in range(2, num+1):  # 2부터 자기자신범위까지 체크하기떄문에 + 1해줌
            if num % i == 0:
                check += 1  # 1개면 나눠지는값이 자기자신뿐이라는것
        if check == 1:  # 1개만있으면 자시자신만 나눠진것
            result += 1  # 소수 1개플러스
print(result)
