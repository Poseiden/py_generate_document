import os
import re

def extract_api_tags(file_path):
    content_string = None
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        match = re.search(r'@Api\(tags\s*=\s*\"(.*?)\"\)', content)
        if match:
            content_string = match.group(1)
    return content_string

def process_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            content_string = extract_api_tags(file_path)
            if content_string is not None:
                print(f'{file_path}: {content_string}')

# Take user input for the absolute path
absolute_path = input("Enter the absolute path: ")

# Check if the entered path exists
if os.path.exists(absolute_path):
    process_directory(absolute_path)
else:
    print("Invalid path. Please provide a valid absolute path.")
