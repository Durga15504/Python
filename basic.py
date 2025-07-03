def asc(char):
    asc_code=ord(char)
    if asc_code>=65 and asc_code<=90:
        print("uppercase")
    elif asc_code>=97 and asc_code<=122:
        print("lowercase")
    elif asc_code>=48 and asc_code<=57:
        print("digits")
    else:
        print("special character")
asc("-")




def ascii(word):
    new_str=""
    for i in range(len(word)):
        code=ord(word[i])
        v=word[i]
        if v=='a' or v=='e' or v=='i' or v=='o' or v=='u':
            new_word=chr(code+1)
            new_str+=new_word
        else:
            new_str+=word[i]
    print(new_str)
ascii("hello")