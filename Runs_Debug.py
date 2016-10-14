s = input("Input Binary String: ")
def e_i(i):
    return (n - i + 3)/(2**(i+2))
def runs_test(s):
    k = 1 #computes k
    n = len(s)
    s_list = []
    t = (n - k + 3)/(2 ** (k + 2)) >= 5
    while t == True:
        k = k + 1
    if t == False:
        k = k - 1
    j = 0 
    '''while j <= n - 2:
        lower = j
        while s[j] == s[j+1]:
            j = j + 1
            if j == n - 1:
                j = n - 2
                break
        j = j + 1
        upper = j
        s_list.append(s[lower:upper])'''
    while j < n:
        lower = j
        if j != 0:
            while s[j] == s[j-1]:
                j = j + 1
                if j == n - 1:
                    break
        j = j + 1
        upper = j
        s_list.append(s[lower:upper])
    return s_list
print(runs_test(s))
