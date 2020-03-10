def solution(s):
    s1 = []
    for i,x in enumerate(s):
        if x == x.upper():
            s1.append(' ')
        s1.append(x)
    return ''.join(s1)
    pass
