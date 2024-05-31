########## Ashraful Hoda 31st May 2024 #############

user_input = input("Enter a string: ")
base_chars = list(user_input)

# Combining characters
combining_right_arrow_above = '\u035B'
combining_left_arrow_above = '\u035C'

# Number of times each combining character is repeated
repeats_right = 5
repeats_left = 15

# Constructing the string
result = ""
for base in base_chars:
    result += base + combining_right_arrow_above * repeats_right + combining_left_arrow_above * repeats_left

print(result)



