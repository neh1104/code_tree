S, Q = input().split()
Q = int(Q)
s = S

for _ in range(Q):
    q = input()
    ft = q[0]
    if ft == '1':
        q = q.split()
        sd = int(q[1])-1; td = int(q[2])-1
        if sd < td:
           ans = s[:sd]+s[td]+s[sd+1:td]+s[sd]+s[td+1:]
        else:
            ans = s[:td]+s[sd]+s[td+1:sd]+s[td]+s[sd+1:]
        print(ans)
        
    else:
        sd = q[2]; td = q[4]
        ans = ''
        for i in s:
            if i == sd:
                ans += td
            else:
                ans += i
        print(ans)
    s = ans
