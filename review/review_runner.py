from review.utils import get_all_java_files, read_file_content
from review.analyzer import analyze_java_code

def run_review():
    java_files = get_all_java_files()
    print("Java files changed:", java_files)

    for file in java_files:
        code = read_file_content(file)
        feedback = analyze_java_code(file, code)
        if feedback:
            print(f"\n📋 Review for {file}:")
            for msg in feedback:
                print(" -", msg)
        else:
            print(f"\n✅ {file}: No issues found.")

if __name__ == "__main__":
    run_review()
