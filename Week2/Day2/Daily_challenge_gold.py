
import re

MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%''' 

# Step 1: Convert matrix_string to a 2D list (matrix)
lines = MATRIX_STR.strip().splitlines()
matrix = []

for line in lines:
    matrix.append(list(line))

num_rows = len(matrix)
num_cols = len(matrix[0])

raw_text = ""

for col in range(num_cols):
    for row in range(num_rows):
        char = matrix[row][col]
        raw_text += char 



decoded_message = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', raw_text)

print(decoded_message)
        

