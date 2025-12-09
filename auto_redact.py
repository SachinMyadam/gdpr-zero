import re
import sys

# Define the file path
log_path = "logs/app.log"

print(f"🔧 Starting auto-redaction on {log_path}...")

try:
    # 1. Read the file
    with open(log_path, "r") as f:
        content = f.read()

    # 2. Define the PII Pattern (password=...)
    pii_pattern = r"password=\S+"

    # 3. Check if leak exists
    if re.search(pii_pattern, content):
        # 4. Replace with redaction
        clean_content = re.sub(pii_pattern, "password=****", content)
        
        # 5. Overwrite the file
        with open(log_path, "w") as f:
            f.write(clean_content)
            
        print("✅ FIXED: Passwords redacted successfully.")
    else:
        print("✅ NO LEAKS: File is already clean.")

except FileNotFoundError:
    print(f"❌ Error: File {log_path} not found.")
    sys.exit(1)
