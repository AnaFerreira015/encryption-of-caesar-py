' TODO: Corrigir padrão de codificação (utf-8)'
message = input('Insert the message: ')
key = int(input('Insert the key: '))

size = len(message)

cript = ''
decrypt = ''

for i in range(size):
    cript += chr(ord(message[i]) + key)
for i in range(size):
    ' TODO: Corrigir decrypt'
    decrypt += chr(ord(cript[i]) - key)

print()
print('Encrypt message: ' + cript)
print('Decrypt message: ' + decrypt)