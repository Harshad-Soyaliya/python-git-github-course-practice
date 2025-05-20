
# Write a python function to remove a given word from a list ad strip it at the same time.

word = input("Enter a word: ").strip().lower()

words = ["hello", "harshad", "h", "m"]
print("Original list:", words)

def removew(w, word_list):
    n = []
    for i in word_list:
        if i.strip().lower() != w:
            n.append(i.strip())
    return n

words = removew(word, words)
print("Updated list:", words)



