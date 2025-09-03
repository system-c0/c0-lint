#!/bin/bash

# Ten skrypt uruchamia wszystkie lintery na podanym pliku
# i kończy działanie z kodem błędu, jeśli którykolwiek z nich zawiedzie.

# Znajdź ścieżkę do folderu, w którym znajduje się ten skrypt
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

TARGET_FILE=$1
FINAL_EXIT_CODE=0

echo "Running all linters on $TARGET_FILE"

# Uruchom C0 Purity Lint, podając pełną ścieżkę
python3 "$SCRIPT_DIR/c0-purity-lint.py" $TARGET_FILE
if [ $? -ne 0 ]; then
    echo "C0 Purity Lint FAILED"
    FINAL_EXIT_CODE=1
fi

# Uruchom E1 Cross-Ref Lint, podając pełną ścieżkę
python3 "$SCRIPT_DIR/e1-cross-ref-lint.py" $TARGET_FILE
if [ $? -ne 0 ]; then
    echo "E1 Cross-Ref Lint FAILED"
    FINAL_EXIT_CODE=1
fi

echo "All linters finished."
exit $FINAL_EXIT_CODE