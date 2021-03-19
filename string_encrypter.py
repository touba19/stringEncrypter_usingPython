print(" ")
print("  ***** Message Encrypter *****")
print(" ")
msg = input("Enter a string you want to Encrypt : ")
print(" ")
msg = list(msg)
n = 0
while n != len(msg):
    if msg[n] == 'W' or msg[n] == 'X' or msg[n] == 'Y' or msg[n] == 'Z' or msg[n] == 'w' or msg[n] =='x' or msg[n]== 'y' or msg[n]== 'z':
       msg[n] = chr(ord(msg[n]) - 22)
       n = n + 1
    else:
       msg[n] = chr(ord(msg[n]) + 4)
       n = n + 1

print("Encrypted String : ")
# using list comprehension 
listToStr = ''.join(map(str, msg))
print(listToStr)
print(" ")