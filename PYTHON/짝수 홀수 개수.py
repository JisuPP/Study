def solution(num_list):
    odd = 0
    even = 0

    for num in num_list:
        if num%2 != 0:
            odd += 1
        else:
            even += 1
    
    return [even, odd]

#######################

def solution(num_list):
    ans = [0, 0]
    for n in num_list:
        ans[n%2] += 1
    return ans

# 1. ans = [0, 0]:
# ans는 두 개의 요소를 가진 리스트입니다.
# ans[0]은 짝수의 개수를 저장하고, ans[1]은 홀수의 개수를 저장합니다.
# 처음에는 두 개의 값이 모두 0으로 초기화됩니다.

# 2. for n in num_list::
# num_list의 각 요소를 하나씩 순회합니다.
# 각 숫자 n에 대해 짝수인지 홀수인지 판단합니다.

# 3. ans[n % 2] += 1:
# n % 2는 숫자 n이 짝수인지 홀수인지를 판별합니다.
# n % 2 == 0: n이 짝수일 때, ans[0]에 1을 더합니다.
# n % 2 == 1: n이 홀수일 때, ans[1]에 1을 더합니다.
# 즉, n % 2가 0이면 ans[0]을 증가시키고, 1이면 ans[1]을 증가시킵니다.

# 4. return ans:
# 짝수와 홀수의 개수를 담고 있는 리스트 ans를 반환합니다.