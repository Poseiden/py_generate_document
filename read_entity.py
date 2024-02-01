import os
import re

def extract_chinese_words(file_path):
    chinese_words = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            matches = re.findall('[\u4e00-\u9fa5]+', line)  # Extract Chinese words from the line
            chinese_words.extend(matches)
            
            # Check for the presence of "public class" and finish reading the file
            if re.search(r'\bpublic\s+class\b', line):
                break
    
    return chinese_words

def process_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            
            chinese_words = extract_chinese_words(file_path)
            if chinese_words:
                print(f'{file_path}: {" ".join(chinese_words)}')

# Take user input for the absolute path
absolute_path = input("Enter the absolute path: ")

# Check if the entered path exists
if os.path.exists(absolute_path):
    process_directory(absolute_path)
else:
    print("Invalid path. Please provide a valid absolute path.")
