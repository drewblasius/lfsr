#Runs Statistical Tests on Pseudorandom Numbers
#Andrew Morrison Blasius
from scipy import stats
def monobit(s): #Runs the Monobit Test #DOF = 1
        n = len(s)
        n_1 = 0
        n_0 = 0
        for i in range(0, len(s)):#Checks for 1s
                if s[i] == "1":
                        n_1 = n_1 + 1
        n_0 = len(s) - n_1 #Computes number of 0s
        X_1 = ((n_0 - n_1)**2)/n #Calculates X_1
        return [X_1,1]
def twobit(s): #Runs the Two-Bit Test #DOF = 2
        n = len(s)
        n_1 = 0
        n_0 = 0
        for i in range(0, len(s)): #Couns number of 1s
                if s[i] == "1":
                        n_1 = n_1 + 1
        n_0 = len(s) - n_1#Computes number of 0s
        n_11 = 0
        n_10 = 0
        n_01 = 0
        n_00 = 0
        for i in range(0, len(s)-1):#Counts number of 00s,01s,10s and 11s
                if s[i]+s[i+1] == "11":
                        n_11 = n_11 + 1
                elif s[i]+s[i+1] == "10":
                        n_10 = n_10 + 1
                elif s[i]+s[i+1] == "01":
                        n_01 = n_01 + 1
                else:
                        n_00 = n_00 + 1
        X_2 = (4/(n-1))*(n_00**2 + n_01**2 + n_10**2 + n_11**2) - (2/n)*(n_0**2 + n_1**2) + 1
        return [X_2,2]
def poker(s): #Runs the Poker Test
        n = len(s)
        m = 1
        poker_sum = 0
        poker_testsum = 0
        t = True
        while t == True: #Picks largest m satisfying given relation
                t = (n//m) >= 5 * 2**m
                if t == True:
                        m = m + 1
                else:
                        m = m - 1
        k = n//m
        s_list = []
        for i in range(0,k): #Changes string into list in preparation for comparison
                s_list.append(s[m*i:m*(i+1)])
        while s_list != []: #Computes Summation Term
            n_i = 0
            test_element = s_list[0]
            n_i = s_list.count(test_element)
            for j in range(n_i):
                s_list.remove(test_element)
            poker_sum = poker_sum + (n_i)**2
        X_3 = ((2 ** m) / k) * poker_sum - k
        return [X_3, 2**m - 1]

def runs(s): #Runs the Runs Test #DOF = 2k - 2
        n = len(s)
        def e_i(i_0): #e_i function
                return (n - i_0 + 3)/(2 ** (i_0 + 2))
        i = 0
        runlist = []
        while (i <= n - 2): #Builds lists of runs
            lower = i
            while (s[i] == s[i + 1]):
                if i == n - 2:
                    break
                i = i + 1
            i = i + 1
            upper = i
            runlist.append(s[lower:upper])
        if (s[n-1] == s[n-2]):
            last_entry =runlist[len(runlist) - 1]
            del runlist[len(runlist) - 1]
            runlist.append(s[n-1] + last_entry)
        else:
            runlist.append(s[n-1])
        i = 0
        while (True == True):
            if (e_i(i) < 5):
                k = i - 1
                break
            i = i + 1
        gapsum = 0
        blocksum = 0
        for element in runlist:#Counts the runs of 0s and 1s
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
        return [X_4,(2*k-2)]           
def auto(s): #Runs the autocorrelation test
    X_5 = 0
    k = 0
    n = len(s)
    d = (len(s)//2) - k #picks d
    A = 0
    for i in range(0, n - d):
        A = A + (int(s[i]) ^ int(s[i + d])) #Computes A(d)
    X_5 = ((2*A - n + d)/((n - d)**(.5)))**2 #Computes (X_5)^2
    return [X_5,1]
def chi(X_i, alpha): #Runs hypothesis test
        p = 1 - stats.chi2.cdf(X_i[0],X_i[1])
        if p < alpha:
                return "FAIL"
        else:
                return "PASS"
s = input("Input Binary String")
alpha = float(input("Input Alpha: "))
print("Enter","\n","1 FOR MONOBIT TEST","\n","2 FOR TWO-BIT TEST","\n","3 FOR POKER TEST","\n","4 FOR RUNS TEST","\n","5 FOR AUTOCORRELATION TEST","\n","6 FOR ALL TESTS")
test = input(":")
if test == "1":
        print("MONOBIT TEST:")
        print("Chi-Square Value:",monobit(s)[0])
        print("Degrees of Freedom:",monobit(s)[1])
        print(chi(monobit(s),alpha))
if test == "2":
        print("TWO-BIT TEST:")
        print("Chi-Square Value:",twobit(s)[0])
        print("Degrees of Freedom:",twobit(s)[1])
        print(chi(twobit(s),alpha))
if test == "3":
        print("POKER TEST:")
        print("Chi-Square Value:",poker(s)[0])
        print("Degrees of Freedom:",poker(s)[1])
        print(chi(poker(s),alpha))
if test == "4":
        print("RUNS TEST:")
        print("Chi-Square Value:",runs(s)[0])
        print("Degrees of Freedom:",runs(s)[1])
        print(chi(runs(s),alpha))
if test == "5":
        print("AUTOCORRELATION TEST:")
        print("Chi-Square Value:",auto(s)[0])
        print("Degrees of Freedom:",auto(s)[1])
        print(chi(auto(s),alpha))
if test == "6":
        print("MONOBIT TEST:")
        print("Chi-Square Value:",monobit(s)[0])
        print("Degrees of Freedom:",monobit(s)[1])
        print(chi(monobit(s),alpha))
        print("TWO-BIT TEST:")
        print("Chi-Square Value:",twobit(s)[0])
        print("Degrees of Freedom:",twobit(s)[1])
        print(chi(twobit(s),alpha))
        print("POKER TEST:")
        print("Chi-Square Value:",poker(s)[0])
        print("Degrees of Freedom:",poker(s)[1])
        print(chi(poker(s),alpha))
        print("RUNS TEST")
        print("Chi-Square Value:",runs(s)[0])
        print("Degrees of Freedom:",runs(s)[1])
        print(chi(poker(s),alpha))
        print("AUTOCORRELATION TEST:")
        print("Chi-Square Value:",auto(s)[0])
        print("Degrees of Freedom:",auto(s)[1])
        print(chi(auto(s),alpha))
quitter = input()
