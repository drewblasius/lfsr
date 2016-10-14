#Andrew Morrison Blasius - Fibonacci LFSR - Emulates a Fibonacci LFSR
print("LFSR runs from right to left! First bit on left becomes part of the keystream!")
print("Taps are labeled from left to right! First tap is on the furthest left!")
n = input("Input LFSR Length")
n = int(n)
taps = eval(input("Input list of taps"))
keylength = int(input("Input length of keystream"))
seed = input("Input Seed")
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
print(LFSR(n,taps,seed,keylength)[0])
quitter = input()
