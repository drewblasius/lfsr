s = input()
s2 = []
i = 0
s3 = []
for i in range(len(s)):
    s2.append(s[i])
while i < len(s2):
    string = s2[i]
    if i == len(s2) - 1:
        if s2[i] == s2[i-1]:
            s2[i-1] = s2[i-1] + s2[i]
            del s2[i]
            break
    else:
        while s2[i] == s2[i+1]:
            string = string + s2[i+1]
            
            i = i + 1
    
print(s2,len(s2))

