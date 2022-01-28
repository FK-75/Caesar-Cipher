def Caesar_cipher(words): # def <<function_name>>(<<parameter>>) in this user defined function Caesar_cipher is the function name I have used because that is the name of the type of cipher being used.

# This part below will describe to the user what the function does and what to input.
# ("str") -> 'str' is the type contract part of the section. This tells the user what type of data is going into the function and what is coming out.
# The part below that is the main description. This can be used by the user to understand what the function does and how it works.

# >>> Caesar_cipher("Vagebqhpgbel Pbzchgre Fpvrar nffvtazrag 7563 grez 7!!")
   # 'Introductory Computer Sciene assignment 2018 term 2!!'
# This part of the section below is the example and Test part of the description. This is used to show an example of the function when being used and what information should be expected. This will be used later by a doc test to check if the correct information is outputted by the code. 
   
    """ ("str") -> 'str' 
    A very simple encryption technique in which each letter in the
    plain text is replaced by a letter some fixed number of positions down the alphabet. This uses ROT-13 for alphabets and
    ROT-5 for digits and can special letters (for example: space, ?, !, #) by not making any
    change to these letters.

    >>> Caesar_cipher("Vagebqhpgbel Pbzchgre Fpvrar nffvtazrag 7563 grez 7!!")
    'Introductory Computer Sciene assignment 2018 term 2!!'
    """
# this is the <<block>> section of the function, this is the main code that will be executed when the function is called. 

    cipher = {"a":"n","b":"o","c":"p","d":"q","e":"r","f":"s","g":"t","h":"u","i":"v","j":"w","k":"x","l":"y","m":"z"} # This is the cipher for the words. The key is the first 13 letters of the alphabet and the value of each character is the corresponding 13 character 13 places from the original. for example, a:n, b:o, etc. 
    cipher_num = {"0":"5","1":"6","2":"7","3":"8","4":"9"} # This is the cipher for the numbers. The key is the first 5 numbers from 0-9 and the value of each number is the corresponding 5 digits 5 places from the original. for example, 0:5, 1:6, etc. 
    result = '' # This is an empty string that will store the result of the cipher.
    for letter in words: # This goes through each letter in the word entered by the user
        if letter.isalpha(): # if the character in the word is from the alphabet then the following code is executed.
            for key, value in cipher.items(): # it goes through each key and value in the cipher dictionary which contains the alphabet split with the first 13 letters being the keys and the second set of 13 being the values of the corresponding letters. e.g. 'a':'n'
                if letter.lower() == key: # this converts the letters entered to lowercase and checks if the letter is equal to one of the keys in the dictionary (first 13 letters).
                    if letter.islower(): # if the statement above is true then if the letter was originally lower case. it adds the value of the key to the results string.
                        result += value
                    elif letter.isupper(): # if the statement above is true then if the letter was originally upper case. it adds the value of the key to the results string and changes the case to an uppercase letter.
                        result += value.upper()
                elif letter.lower() == value: # this converts the letters entered to lowercase and checks if the letter is equal to one of the value in the dictionary (second set of 13 letters).
                    if letter.islower(): # if the statement above is true then if the letter was originally lower case. it adds the key for the value to the results string.
                        result += key 
                    elif letter.isupper(): # if the statement above is true then if the letter was originally upper case. it adds the key for the value to the results string and changes the case to an uppercase letter.
                        result += key.upper()
        elif letter.isdigit(): # if the character in the word is not from the alphabet then the code checks if it is a digit. if so then the following code is executed.
            for key, value in cipher_num.items(): # it goes through each key and value in the cipher_num dictionary.
                if letter == key: 
                    result += value # if the number in the word entered is in the key section of the dictionary then the value of the key is taken and added to the result string.
                elif letter == value: # however if the number in the word entered is in the value section of the dictionary then the key of the value is taken and added to the result string.
                    result += key
        else: # the character is not a letter or a digit then it is a special character.
            result += letter # because the character is a special character then nothing happens to it. it is left and added to the results string. 
    return result # this returns the final result encoded or decoded. 

# This is the test part of the user defined function. it will run an automatic test.
import doctest # the doctest module searches for interactive python sessions and executes it to check if they work exactly as shown. 
doctest.testmod(verbose=True) # This is the type of test being ran. verbose being true means that information is printed about each example, as it is run and an output is displayed even if there are no failures. if it was false,  then only failures are printed.  


phrase = input('\nPlease enter your phrase: ') # This is a user input where the user is asked to enter a phrase or sentence that they want to encode or decode.
print(Caesar_cipher(phrase)) # this will encode or decode the phrase given by the user and will display the result.

# The user can use the code in one of two ways:
    # 1. by calling the function and putting the phrase in quotation marks in the parameter of the function. e.g. Caesar_cipher("Vagebqhpgbel Pbzchgre Fpvrar nffvtazrag 7563 grez 7!!")
    # 2. by entering the phrase or sentence they want to encode or decode when the user is prompted by the code using the code above.
    
