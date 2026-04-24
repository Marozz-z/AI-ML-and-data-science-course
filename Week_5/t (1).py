# Write a Python function that takes a list of words and return the longest word and
# the length of the longest one (Longest word: Exercises Length of the longest word: 9)

def take_list(l):
    maxW = l[0]
    for i in l:
        if len(i) > len(maxW):
            maxW = i
    return  maxW ,len(maxW)

l = list((input("Enter words into the list: ").split()))
t = take_list(l)
print(f"The longest word is {t} and its length is {len(t[0])}")