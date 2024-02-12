import re
import os

# Task 2
# (1)
example_sentence = "Today - on 2024-02-13 - we are sitting in room X-A2-103 and attending a Python workshop. At 12.00 we finally go to the Mensa."

# (2)
output = re.findall(r'\d+', example_sentence)
print(output)

# (3)
output2 = re.findall(r'\w+-\w+-\d+', example_sentence)
print(output2)

# (4)
output3 = re.findall(r'\b[a-z]+\b', example_sentence)
print(output3)

# (5)
output4 = re.findall(r'([A-Z]-)([A-Z]\d-)(\d{3})', example_sentence)
print(output4)
for match in output4:
    print(match)
    example_sentence = re.sub(match[2], '104', example_sentence)
print(example_sentence)

# (6a)
output5= re.split(r'\.\W', example_sentence)
print(output4)

# (6b)
output6 = re.sub(r"\d{4}-\d{2}-\d{2}", "XXXX-XX-XX", output5[0])
print(output5)


###############################################################################

# Task 3
# (1)

def clean_text(input_text):
    cleaned_text = input_text.strip()
    
    # Remove "-" at the end of a line
    cleaned_text = re.sub(r'-\n', '', cleaned_text)

    # Remove more than one whitespace
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

    # Replace ":" with "i" inside words
    matches = re.findall(r'(\b\w*)(:)(\w*\b)', cleaned_text)
    for match in matches:
        cleaned_text = re.sub(match[1], 'i', cleaned_text)

    # Replace "4" with "A" inside words. This is another way to do it.
    A_replacement_pattern = r'(\b\w*)(4)(\w*\b)'
    cleaned_text = re.sub(A_replacement_pattern, r'\1A\3', cleaned_text)

    return cleaned_text

# Example usage
input_text = """
There was noth:ng so VERY remarkable in that; nor d:d Alice
think it so VERY much out of the way to hear the Rabbit say to
itself, `Oh dear! Oh dear! I shall be late!' (when she thought
it over afterwards, it occurred to her that she ought to have
wondered at this, but at the t:me it all seemed quite natural);
but when the Rabbit actually TOOK A WATCH OUT OF ITS WAISTCO4T-POCKET, and 
looked at it, and then hurried on, 4lice start-
ed to
her feet, for it flashed across her m:nd that she had never
before seen a rabbit with e:ther a waistcoat-pocket, or a watch to
take out of it, and burn-
ing with curiosity, she ran across the
field after it, and fortunately was just in t:me to see it pop
down a large rabbit-hole
under the hedge.
"""

result = clean_text(input_text)
print(result)


###############################################################################

# Task 4

def clean_file(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()

    cleaned_content = clean_text(file_content)

    new_file_path = file_path.replace('.txt', '_cleaned.txt')

    with open(new_file_path, 'w') as file:
        file.write(cleaned_content)

# clean_file('projects/group_3/txt-files/alice_1.txt')

###############################################################################

# Task 5

def clean_folder(folder_path):
    
    for file in os.listdir(folder_path):
        if file.endswith('.txt'):
            file_path = folder_path + '/' + file
            clean_file(file_path)

clean_folder('projects/group_3/txt-files')
