# A program to convert any string into Morse Code

morse_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', " ": "·······"}


user_choice = input("Enter 'e' to encrypt a message or 'd' to decrypt it: ").lower()

if user_choice == "e":
    # Encrypting a message to Morse Code
    text_message = input("Enter your message:").upper()

    text_message = [_ for _ in text_message]
    # print(text_message)
    encrypted_message_list = []
    for i in text_message:
        i = morse_dict[i]
        encrypted_message_list.append(i)
        encrypted_message = "".join(encrypted_message_list)
    print(encrypted_message)

elif user_choice == "d":
    # Decrypting a message from Morse Code

    morse_message = input("Enter your Morse coded message:")


    morse_message_list = morse_message.split("·······")
    decrytpted_message_list = []
    for i in morse_message_list:
        decrytpted_message_list.append(i)
                    
            
    print(decrytpted_message_list)
