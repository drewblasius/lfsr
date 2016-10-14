#Clocked Nonlinear Filter with Arnold Cat Map
#Andrew Morrison Blasius
#Using an LFSR of size 18
import math
def LFSR(n,taps,seed,keylength):
    state = []
    keystream = ""
    for i in range(len(seed)):
        state.append(seed[i])
    for i in range(keylength):
        newbit = 0
        for k in taps:
            newbit = (newbit + int(state[k-1])) % 2
        keystream = keystream + str(state[0])
        del state[0]
        state.append(newbit)
    return state
def arnoldcat(xy):
    for i in range(7):
        xy2 = []
        x = xy[0]
        y = xy[1]
        xy2.append((x + y) % 512)
        xy2.append((x+2*y) % 512)
        xy = xy2
    return xy
def filterfunction(x): #Filtering Function - Takes LFSR State as input
    state1 = "0b"
    state2 = "0b"
    for i in range(9):
        state1 += str(x[i])
    for i in range(9,18):
        state2 += str(x[i])
    state1 = int(state1,2)
    state2 = int(state2,2)
    chaosstate = arnoldcat([state1,state2])
    if (state1 > state2):
        return "1"
    if (state1 <= state2):
        return "0"
print("LFSR has 18 Registers")
keylen = int(input("Length of Keystring:"))
state = str(input("Input Seed:"))
variablecycle = input("Variable Cycle [Y/N]:")
def filtergenerator(keylen,state,cycle):
    newkeystream = ""
    for i in range(keylen):
        newkeystream = newkeystream + filterfunction(LFSR(18,[1,8],state,cycle))#Works, single shift state:
        newstate = LFSR(18,[1,8],state,cycle)
        state = ""
        for j in range(len(newstate)):
            state = state + str(newstate[j])                                
    return newkeystream
if (variablecycle == "N"):
    print(filtergenerator(keylen,state,1))
if (variablecycle == "Y"):
    cycle = int(input("Number of Shift Cycles per Filter Cycle:"))
    print(filtergenerator(keylen,state,cycle))
quitter = input()
