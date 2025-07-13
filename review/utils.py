import subprocess

def get_changed_java_files():
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~1"],
        capture_output=True,
        text=True
    )
    return [f for f in result.stdout.splitlines() if f.endswith(".java")]

def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
