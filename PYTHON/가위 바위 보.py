# 가위 2
# 바위 0
# 보 5

def solution(rsp):
    ans = ''
    
    for x in rsp:
        if x == '2':
            ans += '0'
        elif x == '0':
            ans += '5'
        else:
            ans += '2'
    return ans

########################

def solution(rsp):
    d = {'0' : '5', 
         '2' : '0', 
         '5' : '2'}
    return ''.join(d[i] for i in rsp)

def solution(rsp):
    rsp =rsp.replace('2','s')
    rsp =rsp.replace('5','p')
    rsp =rsp.replace('0','r')
    rsp =rsp.replace('r','5')
    rsp =rsp.replace('s','0')
    rsp =rsp.replace('p','2')
    return rsp