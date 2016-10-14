s = input("Input Binary String: ")

def poker(s): #Runs the Poker Test
        n = len(s)
        m = 1
        poker_sum = 0
        poker_testsum = 0
        t = True
        while t == True:
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
        return X_3
print(poker(s))
quitter = input()
