def palindrome(sentence):
    sentence=sentence.split(" ")
    palindrome_count=0
    for i in range(len(sentence)):
        if sentence[i][::-1]==sentence[i]:
            palindrome_count+=1
    print(palindrome_count)
palindrome("my family consists of amma nanna akka anna")