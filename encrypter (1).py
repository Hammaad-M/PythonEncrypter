def encode():
    forward = True
    key = input('enter encryption key: ')
    try:
        key = str(key)
    except ValueError:
        forward = False
    if not forward:
        print('Please enter key as letters.')
        encode()
    text = list(input('enter message you wish to encrypt: '))
    a = 0
    output = ''  
    for i in range(len(text)):
        output += str((ord(text[i])) + ord(key[a]))
        if a < len(key)-1:
            a+=1
        else:
            a = 0

    print(output)
    return

def decode():
    key = input('enter encryption key as letters: ')
    text = input('enter message you wish to decrypt: ')
    processed = []
    
    #text.split(str(text[0]))
    #print(text[1])
    for i in range(0, len(text), 3):
        processed.append(text[i:i+3])
        
    output = []
    a = 0
    
    for i in range(len(processed)):
        output.append(int(processed[i])-ord(key[a]))
        #output += str(int(processed[i])-ord(key[a]))
        if a < len(key)-1:
            a+=1
        else:
            a = 0
    #message = ''
    for i in range(len(output)):
        try:
            output[i] = chr(output[i])
            #message += str(chr(int(output[i])))
            #print(str(chr(int(output[i]))))
        except ValueError:
            print('Incorrect key or encryption entered...')
            break
        
    message = ''
    for i in range(len(output)):
        message += str(output[i])
    print('__MESSAGE__:')
    #print(message)
    print(message)
    return

    
def Launch():
    choice = input('[e]ncode or [d]ecode? ')
    if choice == 'e':
        encode()
    elif choice == 'd':
        decode()
    else:
        Launch()

RUN = True
if __name__ == '__main__':
    while RUN:
        Launch()
        x = input('Hold Enter Key to exit or [c]ontinue: ')
        if x != 'c':
            exit()
            
        
        
