
import re

PATTERNS = [
    ("AWS Access Key ID", re.compile(r"\bA3T[A-Z0-9]{13}\b|\bAKIA[0-9A-Z]{16}\b")),

    ("AWS Secret Access Key",
        re.compile(
            r"(?i)aws(.{0,20})?(secret|secret_access_key|secretKey)(.{0,10})?[:=]\s*[\"']?[A-Za-z0-9/+=]{40}[\"']?"
        )
    ),

    ("Google API Key", re.compile(r"\bAIza[0-9A-Za-z\-_]{35}\b")),

    ("Generic API Key",
        re.compile(
            r"(?i)(api[_-]?key|apikey|token|secret)[\s:=]{0,6}[\"']?[A-Za-z0-9\-_]{16,45}[\"']?"
        )
    ),

    ("JWT", re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\b")),

    ("RSA Private Key Block", re.compile(r"-----BEGIN (RSA |OPENSSH |)PRIVATE KEY-----")),
    ("SSH Private Key", re.compile(r"-----BEGIN OPENSSH PRIVATE KEY-----")),
    ("PGP Private Key Block", re.compile(r"-----BEGIN PGP PRIVATE KEY BLOCK-----")),

    ("Slack Token", re.compile(r"\b(xox[baprs]-[0-9A-Za-z-]{10,})\b")),
    ("Heroku API Key", re.compile(r"\b[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\b")),
    ("Basic Auth in URL", re.compile(r"https?://[^/@\s]+:[^/@\s]+@")),
]
