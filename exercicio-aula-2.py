"""
Given a sentence create and print a new sentence so that 
the first letter of all words is written in upper case
and the other letters as lowercase letters.
Ex: I went to CINEMA A: I Went To Cinema
"""
sentence = ""
while sentence == "":
    sentence = input("Enter a sentence: ")

sentence = sentence.strip()
print(sentence)


new_sentence = ""
for x in range(len(sentence)):
    if x == 0 or (x > 0 and sentence[x - 1] == " " and sentence[x + 1] != " "):
        new_sentence += sentence[x].upper()
    else:
        new_sentence += sentence[x].lower()

print(new_sentence)