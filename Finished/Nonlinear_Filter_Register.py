#Nonlinear Filter
#Andrew Morrison Blasius
#Using an LFSR of size 16
def LFSR(n,taps,seed,keylength):#Emulates A Fibonacci LFSR
    keystream = ""#Keystream (Empty at first)
    registers = []#LFSR State (in list form)
    for i in range(len(seed)):#Works
            registers.append(seed[i])#Takes the ith entry of the keystream and appens to the list in the ith position
    for i in range(keylength):#Works
        newregisters = []#New State (List)
        keystream = keystream + str(registers[0])#Add the last bit to the keystream
        placeholder = 0#Variable used for the feedback operation
        for k in taps:#Picks out each entry in the list taps
            placeholder = (placeholder + int(registers[(k-1)])) % 2#Feedback operation
        for j in range(n-1):
            newregisters.append(registers[j+1])#Appends the i+1th entry to the ith entry of the new state
        newregisters.append(placeholder)#Appends the "feedback bit" to the end of the LFSR
        registers = newregisters#Replaces current state with new state
    return(registers)
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
