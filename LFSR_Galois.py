#Galois LFSR
n = int(input("Length of LFSR: "))
taps = eval(input("List of Taps: "))
key_len = input("Length of Keystream: ")
seed = input("Seed: ")
state = []
key= ""
for i in range(len(seed)):
    state.append(seed[i])
for i in range(key_len)
    key = str(state[0]) + key
    if (int(state[0]) == 0):
        del state[0]
        
