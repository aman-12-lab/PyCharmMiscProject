"""In this exercise create two functions
my_split : which splits sentence given as first argument using second argument as a
separator character to separate list items. Function returns a list of items.
my_join : which joins list given as first argument to a string separated with character given
as second argument. Function returns a string.
In this exercise you are not allowed to use Python split and join functions """

def my_split(s, sep):
    out, word = [], ""
    for c in s:
        if c == sep: out.append(word); word = ""
        else: word += c
    out.append(word)
    return out

def my_join(lst, sep):
    out = lst[0]
    for x in lst[1:]: out += sep + x
    return out

s = input("Please enter sentence:")
w = my_split(s, " ")
print(my_join(w, ","))
for x in w: print(x)
