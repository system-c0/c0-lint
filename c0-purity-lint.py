import sys
import re

def check_purity(file_path):
    print("--- Running C0 Purity Lint ---")
    violations = 0
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Prosta reguła: znajdź słowo "interpretacja" lub "znaczenie"
    forbidden_words = ["interpretacja", "znaczenie", "podobny do", "przypomina"]
    for word in forbidden_words:
        matches = re.finditer(r'\b' + word + r'\b', content, re.IGNORECASE)
        for match in matches:
            violations += 1
            print(f"Violation: Found forbidden word '{word}' at position {match.start()}. C0-core must be free of interpretation.")

    if violations == 0:
        print("C0 Purity Lint: PASS. No interpretative language found.")
        return True
    else:
        print(f"C0 Purity Lint: FAIL. Found {violations} violations.")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if not check_purity(sys.argv[1]):
            sys.exit(1)
    else:
        print("Usage: python c0-purity-lint.py <path_to_tex_file>")
        sys.exit(1)