import os
import javalang

field_names =  []
types = []
documentations = []

def extract_fields_and_annotations(java_file_path):
    
    with open(java_file_path, 'r', encoding='utf-8') as file:
        tree = javalang.parse.parse(file.read())
        
        for path, node in tree.filter(javalang.tree.FieldDeclaration):
            # print(node)
            # print("--------------------------------------------------------------------------------------------------")
            if 'private' in node.modifiers:
                field_names.append(node.declarators[0].name)

                type_name = node.type.name
                if type_name == 'BigDecimal':
                    type_name = 'Decimal'
                elif type_name == 'String':
                    type_name = 'Varchar'
                elif type_name == 'Integer':
                    type_name = 'Int'
                elif type_name == 'Date':
                    type_name = 'Date'
                else:
                    type_name = ' '
                types.append(type_name)

                documentations.append(node.documentation.splitlines()[1])

# Take user input for the Java entity class file path
java_file_path = input("Enter the Java entity class file path: ")

# Check if the entered path exists
if not java_file_path.endswith('.java') or not os.path.exists(java_file_path):
    print("Invalid Java file path. Please provide a valid path to a Java entity class file.")
else:
    extract_fields_and_annotations(java_file_path)
    for _ in field_names:
        print(_)
    for _ in types:
        print(_)
    for _ in documentations:
        print(_)
