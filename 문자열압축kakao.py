s = "abcabcabcabcdededededede"


def solution(s):
    answer = len(s)
    for i in range(1, int(len(s)/2)+1):
        k = 0
        c = 0
        l = ""
        while(k < len(s)):
            if s[k:k+i] == s[k+i:k+i+i]:
                c += 1
            else:
                if c != 0:
                    l += str(c+1)
                    l += s[k:k+i]
                    c = 0
                else:
                    l += s[k:k+i]
            k = k+i
        answer = min(len(l), answer)

    return answer


print(solution(s))
