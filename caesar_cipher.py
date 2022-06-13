
user_string = input("Please Enter text to Cipher \n")
shift_value = input("Please Input The Shifting Value. Use Can use Either a Positive or Negative Value. \n")
shift_value = int(shift_value)
# text_array = user_string.split(word)
# print(text_array)

def split(user_string):
    return [char for char in user_string]
text_array = (split(user_string))
#print(text_array)


univals = []
for t in text_array:
    univals.append(ord(t)+shift_value)
    #print(univals)
    
    #for i in univals:
        #plus1_univals = univals + 1
        #print(plus1_univals)

    #print(type(plus1_univals))
    cipher_text = ''.join(chr(i) for i in univals)

print("The Ciphered Text Is: ", cipher_text)


