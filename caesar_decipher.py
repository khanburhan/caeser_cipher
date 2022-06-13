user_answer = "y"
user_option1 = "n"
user_option2 = "y"


while user_answer == user_option2:
    ciph_string = input("Please Enter Caeser Ciphered Text \n")
    shift_value = input("Please Input The Shifting Value. Use Can use Either a Positive or Negative Value. \n")
    shift_value = int(shift_value)
    # text_array = text1.split(word)
    # print(text_array)
    def split(ciph_string):
        return [char for char in ciph_string]
    text_array = (split(ciph_string))
    #print(text_array)


    univals = []

    for t in text_array:
        univals.append(ord(t)+shift_value)
        #print(univals)
    
        #for i in univals:
            #plus1_univals = univals + 1
            #print(plus1_univals)

        #print(type(plus1_univals))
        deciphered_text = ''.join(chr(i) for i in univals)

    print("The DeCiphered Text Is: ",deciphered_text)

    user_answer = input("Do you want to try again? Please type n for NO and y for YES and press return: ") 


