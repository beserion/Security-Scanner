# Beseri Security Scanner

A lightweight Python tool that detects hardcoded secrets and tokens inside source files.
Can be used manually or as a Git pre-commit hook.

## Features
- Detects AWS, Google, JWT, private keys, slack tokens, and generic API keys
- Recursive directory scanning
- Non-zero exit on secret detection (CI/CD & hooks)
- Flexible and easy-to-extend regex patterns

## Usage
```
python3 scanner.py .
```

- minor update @ 2026-01-10 21:00:57.465603
- minor update @ 2026-01-10 21:00:57.707805