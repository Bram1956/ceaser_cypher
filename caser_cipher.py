
LAST_CHAR_CODE=ord("Z")
FIRST_CHAR_CODE=ord("A")
CHAR_RANGE=LAST_CHAR_CODE-FIRST_CHAR_CODE+1


def caeser_text(message,shift):
    #result
    result=""

    #looping
    for char in message.upper():
        #ascii code
        if char.isalpha():
            char_code=ord(char)

            new_char_code=char_code+shift
            
            if new_char_code>LAST_CHAR_CODE:

                new_char_code-=CHAR_RANGE
            
              
            if new_char_code<FIRST_CHAR_CODE:

                new_char_code+=CHAR_RANGE


            new_char=chr(new_char_code)
            result+=new_char
            
        else:
            result+=char

    return(result)

#user input
# user_message=input("Message to Encrpyt: ")
# user_shift_key=int(input("Shift Key(integer): "))

# caeser_text(user_message,user_shift_key)
# caeser_text()

sys.modules[__ceaser_text__]=caeser_text