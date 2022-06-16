
import string
user_string = input("Please Enter text to Cipher\n").lower()
shift_value = input(
    "Please Input The Shifting Value. Use Can use Either a Positive or Negative Value. \n")

print(user_string)
shift_value = int(shift_value)
# text_array = user_string.split(word)
# print(text_array)


def split(user_string):
    return [char for char in user_string]


text_array = (split(user_string))
# print(text_array)


univals = []
new_univals = []
for t in text_array:
    univals.append(ord(t)+shift_value)
    # print(univals)
for x in univals:
    if x == 32:
        new_univals.append(x)
    elif x > 122:
        new_univals.append((x - 122) + 96)
    elif x < 96:
        new_univals.append(x + 122)
    else:
        new_univals.append(x)
    # print(new_univals)
""" for p in new_univals:
    print(p)
    print(chr(p)) """

cipher_text = ''.join(chr(i) for i in new_univals)
# print(univals)

print("The Ciphered Text Is: ", cipher_text)
