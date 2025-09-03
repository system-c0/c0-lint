import sys
import re

def check_e1_references(file_path):
    print("--- Running E1 Cross-Reference Lint ---")
    violations = 0
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Prosta reguła: znajdź odwołania do [E1]
    e1_references = re.finditer(r'\[E1\]', content)
    for match in e1_references:
        violations += 1
        print(f"Violation: Found a reference to [E1] at position {match.start()}. C0-core cannot reference the E1 layer.")

    if violations == 0:
        print("E1 Cross-Ref Lint: PASS. No references to E1 found.")
        return True
    else:
        print(f"E1 Cross-Ref Lint: FAIL. Found {violations} violations.")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if not check_e1_references(sys.argv[1]):
            sys.exit(1)
    else:
        print("Usage: python e1-cross-ref-lint.py <path_to_tex_file>")
        sys.exit(1)