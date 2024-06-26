##try: 
##    raise NameError("Hi there")
##except:
##    print ("An exception")
##    raise


#to list exception handling
##print(dir(locals()["__builtins__"]))

#dictionary task

input_string = "sharmila"
letter_counts = {}

for letter in input_string:
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1

print(letter_counts)  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
