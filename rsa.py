import math

#print("Введите ваше сообщение")
#message=89#input()
print ("Введите два числа")
p=3#input()
q=7#input()
n=p*q
fincEilera=(p-1)*(q-1)
print ("Введите эту маленькую экспаненту тип шобы она была тип простое 3,5,7 и чтобы меньше ", n)
e=5#input()
print ("Открытый ключ - пара ",e ," и ",n )

#--------------------------------------------------------------------------------------------------
#Тпепрь нам нужно такое d, шобы в следующей формуле остаток от деления короче 1 было 
d=2 
while ((d*e)%fincEilera!=1):
    d+=1
    print ("Твоё d: ",d)
#(d*e)%fincEilera=1
print ("Закрытый ключ - пара ",d ," и ",n )


print ("Введите вашу смс-ку:")
p=19
print ("Ваше сообщение:",p)

def encrypt():
    encryptmessage=math.pow(p,e)%n
    print ("Зашифрованное сообщение:",encryptmessage) 
    return encryptmessage   

encryptmessage=encrypt()

def decrypt():
    decryptmessage=math.pow(encryptmessage,d)%n
    print("Расшифрованное сообщение:",decryptmessage)
    return decryptmessage

decryptmessage=decrypt()

message="Hello World"
binarymessage=0
def toBinary(a):
  global binarymessage
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
    binarymessage = m
  return m

print(message," in binary is ") 
print(toBinary(str(message)))
print(type(binarymessage))
print (binarymessage[0])
print (len(message))
#for i in range(len(message)):
    #p=binarymessage[i]
    #encryptmessage=encrypt()
    #decryptmessage=decrypt()
    
