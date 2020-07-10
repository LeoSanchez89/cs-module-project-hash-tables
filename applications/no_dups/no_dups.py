def no_dups(s):
    # Your code here
    no_dupes = []
    words = s.split()
    for word in words:
        if word not in no_dupes:
            no_dupes.append(word)
    return " ".join(no_dupes)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))