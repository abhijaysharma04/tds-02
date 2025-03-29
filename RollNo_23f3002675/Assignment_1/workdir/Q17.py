import os

# Set absolute path (adjust if needed)
base_dir = r"C:\TDS-02\RollNo_23f3002675\Assignment_1\workdir\q-compare-files"
file1 = os.path.join(base_dir, "a.txt")
file2 = os.path.join(base_dir, "b.txt")

# Check if files exist
if not os.path.exists(file1):
    print(f"❌ File not found: {file1}")
    exit(1)
if not os.path.exists(file2):
    print(f"❌ File not found: {file2}")
    exit(1)

# Read lines
with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

# Compare line by line
if len(lines1) != len(lines2):
    print("⚠️ Warning: Files have different number of lines")

# Count mismatched lines
diff_count = sum(1 for a, b in zip(lines1, lines2) if a.strip() != b.strip())

print(f"✅ Number of differing lines: {diff_count}")
