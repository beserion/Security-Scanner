import os
import sys
import re
import patterns

ALLOWED_EXT = [".py", ".env", ".txt", ".json", ".yaml", ".yml"]

def color(text, code):
    return f"\033[{code}m{text}\033[0m"

def get_files(path):
    files = []
    for root, dirs, filenames in os.walk(path):
        for f in filenames:
            full = os.path.join(root, f)

            if full.endswith("patterns.py"):
                continue

            if not any(full.endswith(ext) for ext in ALLOWED_EXT):
                continue

            files.append(full)
    return files

def scan_file(file_path):
    results = []
    try:
        with open(file_path, "r", errors="ignore") as f:
            lines = f.readlines()
            for idx, line in enumerate(lines, 1):
                for name, pattern in patterns.PATTERNS:
                    if pattern.search(line):
                        results.append((idx, name, line.strip()))
    except:
        pass
    return results

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    files = get_files(target)
    found_any = False

    for file_path in files:
        matches = scan_file(file_path)
        if matches:
            found_any = True
            print(color(f"==> {os.path.basename(file_path)}", "33"))
            for line_no, name, content in matches:
                print(f"  {line_no}: [{name}] {content}")

    if found_any:
        print(color("\nSecrets detected.", "31"))
    else:
        print(color("No secrets found.", "32"))

if __name__ == "__main__":
    main()
