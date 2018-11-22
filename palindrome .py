user_input=input("Enter a word:")

user_word_list=list(user_input.lower())

user_word_list_reverse=user_word_list[::-1]

if(user_word_list == user_word_list_reverse):
    print("The word is palindrome ")
else:
    print("The word is Not palindrome ")