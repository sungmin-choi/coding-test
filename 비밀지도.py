def solution(n, arr1, arr2):
    answer = []
    for num1, num2 in zip(arr1, arr2):
        tmp = str(bin(num1 | num2))[2:]
        if len(tmp) < n:
            tmp = '0'*(n-len(tmp))+tmp
            tmp = tmp.replace('1', '#')
            tmp = tmp.replace('0', ' ')
            answer.append(tmp)
        return answer
