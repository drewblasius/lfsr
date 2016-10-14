#Clocked Nonlinear Filter with Arnold Cat Map
#Andrew Morrison Blasius
#Using an LFSR of size 16
def LFSR(n,taps,seed,keylength):#Emulates A Fibonacci LFSR
    keystream = ""
    registers = []
    for i in range(len(seed)):#Works
            registers.append(seed[i])
    for i in range(keylength):#Works
        newregisters = []
        keystream = keystream + str(registers[0])
        placeholder = 0
        for k in taps:
            placeholder = (placeholder + int(registers[(k-1)])) % 2
        for j in range(n-1):
            newregisters.append(registers[j+1])
        newregisters.append(placeholder)
        registers = newregisters
    return(registers)
def arnoldcat(xy):
    for i in range(7):
        xy2 = []
        x = xy[0]
        y = xy[1]
        xy2.append((x + y) % 512)
        xy2.append((x+2y) % 512)
        xy = xy2
    return xy
def filterfunction(x): #Filtering Function - Takes LFSR State as input
    state1 = "0b"
    state2 = "0b"
    for i in range(9):
        state1 += str(x[i])
    for i in range(9,18):
        state2 += str(x[i])
    state1 = int(state1)
    state2 = int(state2)
    return [state1,state2]    
print("LFSR has 16 Registers")
key = int(input("Length of Keystring:"))
state = str(input("Input Seed:"))
variablecycle = input("Variable Cycle [Y/N]:")
def filtergenerator(key,state,cycle):
    newkeystream = ""
    for i in range(key):
        newkeystream = newkeystream + str(filterfunction(LFSR(16,[1,2,4,13],state,cycle)))#Works, single shift state:
        newstate = LFSR(16,[1,2,3,4],state,cycle)
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
