import random
import re
# Read in all the data in one go
with open("./applications/markov/input.txt") as f:
    data = f.read()

# TODO: analyze which data can follow other data
# Your code here

words = {}
data = data.split()
for i in range(len(data)-1):
    if not data[i] in words:
        words[data[i]] = [data[i+1]]
    else:
        words[data[i]].append(data[i+1])
start_words = [key for key in words.keys() if re.search(r'^"[A-Z]', key) or re.search(r'[A-Z]', key)]
end_words = [key for key in words.keys() if re.search(r'[?.!]$', key) or re.search(r'[?.!]"$', key)]

# TODO: construct 5 random sentences
# Your code here

for x in range(5):
    print("----------------------")
    end_sentence = False
    finished_sentence = ""
    current_word = random.choice(start_words)
    while not end_sentence:
        finished_sentence = finished_sentence + current_word + ' '
        if current_word in end_words:
            end_sentence = True
            print(finished_sentence)
        else:
            current_word = random.choice(words.get(current_word))
    print("----------------------")