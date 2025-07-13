import os

def get_all_java_files():
    java_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".java"):
                java_files.append(os.path.join(root, file))
    return java_files

def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()