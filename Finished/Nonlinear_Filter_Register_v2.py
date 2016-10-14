#Nonlinear Filter
#Andrew Morrison Blasius
#Using an LFSR of size 16
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
def filterfunction(x): #Filtering Function - Takes LFSR State as input
     while (len(x) != 1):
        x0 = "" 
        y0 = []
        for i in range(len(x)):#Changes the state from a list to a string
            x0 = x0 + str(x[i])
        for i in range(0,len(x),2):#Makes the string into a list
            y0.append(x0[i:i+2])#and separates each string into a list
        x = []
        for element in y0: #XOR operation
            xor = int(element[0]) ^ int(element[1])
            x.append(xor)
     return x[0]
print("LFSR has 16 Registers")
key = int(input("Length of Keystring:"))
state = str(input("Input Seed:"))
variablecycle = input("Variable Cycle [Y/N]:")
def filtergenerator(key,state,cycle):
    newkeystream = ""
    for i in range(key):
        newkeystream = newkeystream + str(filterfunction(LFSR(16,[1,2,4,13],state,cycle)))#Works, single shift state:
        newstate = LFSR(16,[1,2,4,13],state,cycle)
        state = ""
        for j in range(len(newstate)):
            state = state + str(newstate[j])                                
    return newkeystream
if (variablecycle == "N"):
    print(filtergenerator(key,state,1))
if (variablecycle == "Y"):
    cycle = int(input("Number of Shift Cycles per Filter Cycle:"))
    print(filtergenerator(key,state,cycle))
quitter = input()
