# Brian Nordlinger

"""
Returns the number of times the letter "a" appears in a list of strings. We can assume that the list
contains strings or nothing at all. The method uses for loops to iterate through the list of strings,
and then iterate through the strings themselves, incrementing the acount variable everytime the letter 
"a" is found. If the letter "a" does not appear within any of the strings then 0, the default count, 
is returned.
"""

def count_a(words):
    acount = 0
    for i in range(len(words)):
        for y in range(len(words[i])):
            if words[i][y] == "a":
                acount += 1
    return(acount)

"""
Returns the inputed string with a specified letter within the word repeated however many times
is inputted. If the specified letter is not found within the word, returns letter not found. 
The method uses for loops to first search for the specified letter. If the letter is found, it is 
repeated one less than the time inputted, to account for one already existing in the string. Then, the 
original letter is set to null so that it doesn't repeat on the newly added letters.
"""

def multi_letter(word, num, let):
    hit = 0
    for i in range(len(word)):
        if word[i] == let:
            word = word[0:i] + word[i] * (num-1) + word[i:]
            let = None
            hit = 1
    if hit == 0:
        return("letter not found")
    if hit == 1:
        return(word)

#Test Cases

print(count_a(["a","aa","aaa"]))
print(count_a(["bread","tree","grass", "lamb", "fox", "array"]))
print(count_a(["zzz", "yyy", "xxx", "www"]))

print(multi_letter("bread", 3, "a"))
print(multi_letter("cheese", 5, "h"))
print(multi_letter("duck", 2, "a"))
            
    