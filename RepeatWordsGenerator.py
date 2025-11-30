print("***************************************************************************************************************")

print("3. Write a generator function called repeat_word(word, times) that yields the given character char a specified number of times.")

def repeat_word(word, no_of_times):
    for _ in range(no_of_times):
        yield word

word = "hello"
no_of_times = 3

for w in repeat_word(word, no_of_times):
    print(w)

print("***************************************************************************************************************")
