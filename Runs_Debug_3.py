s = input()
n = len(s)
i = 0
runlist = []
while (i <= n - 2):
    lower = i
    while (s[i] == s[i + 1]):
        if i == n - 2:
            break
        i = i + 1
    i = i + 1
    upper = i
    runlist.append(s[lower:upper])
if (s[n-1] == s[n-2]): #Works, but check!
    last_entry =runlist[len(runlist) - 1]
    del runlist[len(runlist) - 1]
    runlist.append(s[n-1] + last_entry)
else:
    runlist.append(s[n-1])
def e_i(i_0):
    return (n - i_0 + 3)/(2 ** (i_0 + 2))
i = 0
while (True == True):
    if (e_i(i) < 5):
        k = i - 1
        break
    i = i + 1
gapsum = 0
blocksum = 0
for element in runlist:
    if len(element) > k:
        runlist.remove(element)
    else:
        if (element[0] == "1"):
            B_i = runlist.count(element)
            blocksum = blocksum + ((B_i - e_i(len(element)))**2)/(e_i(len(element)))
            for i in range(B_i):
                runlist.remove(element)
        else:
            G_i = runlist.count(element)
            gapsum = gapsum + ((G_i - e_i(len(element)))**2)/(e_i(len(element)))
            for i in range(G_i):
                runlist.remove(element)
X_4 = gapsum + blocksum
return X_4
