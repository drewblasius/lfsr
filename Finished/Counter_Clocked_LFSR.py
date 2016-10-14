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
    return [keystream, state]
    
def listtostring(l):
    s = ""
    for i in range(len(l)):
            s = s + str(l[i])
    return s
keystream = ""

print("CLOCK PROPERTIES")
print("Some nice options:","\n","Length = 41","\n","taps = [1,3]")
clocklength = int(input("Length: "))
clocktaps = eval(input("List of taps: "))
clockseed = input("Seed: ")
countersetting = int(input("Counter Setting:")) #Sets the counter

print("LFSR PROPERTIES","\n","Some nice options:","\n","Length = 84","\n","taps = [1,15]")
keylength = int(input("Desired length of keystream: "))
taps = eval(input("List of taps: "))
n = int(input("Length of LFSR: "))
seed = input("Seed: ")

for i in range(keylength):
    counter1 = 0 #First counter. Counts the number of 1s from the clock LFSR
    counter2 = 0 #Second counter. Counts the number of bits from the clock LFSR
    while (counter1 < countersetting): #Counts the number of bits that pass through the counter before
        clock = LFSR(clocklength,clocktaps,clockseed,1) #the value of the variable countersetting is reached
        nextbit = int(clock[0])
        if (nextbit == 1):
            counter1 = counter1 + 1
        clockseedlist = clock[1]
        clockseed = listtostring(clockseedlist)
        counter2 = counter2 + 1
    newkeybit = str(LFSR(n,taps,seed,counter2)[0])
    newkeybit = newkeybit[(counter2 - 1)]
    keystream = keystream + newkeybit
    seedlist = LFSR(n,taps,seed,counter2)[1]
    seed = listtostring(seedlist)
print(keystream)


