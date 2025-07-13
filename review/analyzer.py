def analyze_java_code(file_path, code):
    feedback = []

    # Example rule: Avoid System.out.println
    if "System.out.println" in code:
        feedback.append("Avoid using System.out.println for logging in production.")

    # You can later plug in a trained model or tokenizer here
    return feedback
