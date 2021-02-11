import string

def word_count(s):
    # Your code here
    repetitions = {}
    ignored = '":;.,-+=/\|[]{}()*^&'
    s = s.lower()
    s = s.translate(str.maketrans({a:None for a in ignored})) #string.punctuation
    words = s.split()
    
    for word in words:
        repetitions[word] = words.count(word)
    return repetitions


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))

