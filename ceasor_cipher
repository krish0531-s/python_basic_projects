
Alphabets = [
    'A', 'B', 'C', 'D', 'E', 'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W', 'X','Y', 'Z'
]

def Encrypt(message, step):
    crypt = []
    for i in range(len(message)):
        index = 0
        for k in range(len(Alphabets)):
            if Alphabets[k] == message[i]:
                index = k
                break
        if index+step<26:
            crypt.append(Alphabets[index+step])
        else:
            t = (index+step)-26
            crypt.append(Alphabets[t])
    return crypt

def Decrypt(crypt, step):
    message = []
    for i in range(len(crypt)):
        index = 0
        for k in range(len(Alphabets)):
            if Alphabets[k] == crypt[i]:
                index = k
                break
        if index-step>0:
            message.append(Alphabets[index-step])
        else:
            t = -1+(index-step)
            print(t)
            message.append(Alphabets[t])
    return message





msg = input('Enter: ').upper()
step = int(input('Enter Step: '))
t = Encrypt(msg, step)
for i in t:
    print(i, end = '')
print('\nDecrypt')
m = Decrypt(t, step)
for i in m:
    print(i, end = '')
