#Runs the Autocorrelation Test
s = str(input("Input String:"))
def autocorrelationtest(s):
    X_5 = 0
    k = 0
    while (X_5 <= 0):
        n = len(s)
        d = (len(s)//2) - k
        d = 8
        A = 0
        for i in range(0, n - d):
            A = A + (int(s[i]) ^ int(s[i + d]))
        X_5 = (2*A - n + d)/((n - d)**(.5))
        k = k + 1
    return X_5

