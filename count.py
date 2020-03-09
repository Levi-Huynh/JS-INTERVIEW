'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.

U
input= 1 string, 
output= integer, tracker of how many times "th" occurs within input string (case sensitive, so TH or Th, or tH doesn't count) 
must use recursion n 

p
-split string into list of char, 
- use find (return index)
-if index > -1  , add to tracker var, slice 
edge cases:
empty str:
returns 0
1 instance:
returns 1
multple:
returns occurences
backwards:

mixedcase: 

- use tracker , Add to tracker everytime "th" appears in list 
- Minus 
-once tracker = len(word) -1 return 
-base case: if 

E

R
'''


def count_th(word):
    mywordlen = len(word)
    key = "th"
    search = word.find(key)
    print("word", word[:2])
    if mywordlen == 0 or search == -1:
        return 0
    if search > -1:
        word = word[(search+2):]

        # take the remaining chars in word, & search for key "th" in remaining char, until
        # search -1, or length of word is 0
    print("word.find(key) index", search)
    print("res", 1 + (count_th(word)))
    # return 1 to keep track of the amount of times  search finds th
    return 1 + count_th(word)


print(count_th("TthHtHthth"))


"""
  else:
        # I will walk through the word looking for the characters specified "th" and if I find them I will return 1
        # plus a recursive search through the rest of the string moving forward 2 spaces, otherwise, I will not add
        # 1 to the value and move forward through the string only one space.
        if word[0:2] == 'th':
            return 1 + count_th(word[2:]) #stops search & returns 1 for each instance th is found, & returns 
            #the function, startting at 2: index & beyond 
        else:
            return count_th(word[1:]) #searches thru all the remaining chars 1 by 1, starts at 1, (the next intsance char)
"""
