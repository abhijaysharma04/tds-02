import os
import shutil
import re
import hashlib

def rename_digits(filename):
    return re.sub(r'\d', lambda m: str((int(m.group()) + 1) % 10), filename)

def prepare_q16_hash(directory, temp_flat_dir):
    if os.path.exists(temp_flat_dir):
        shutil.rmtree(temp_flat_dir)
    os.makedirs(temp_flat_dir, exist_ok=True)

    combined = []

    for root, _, files in os.walk(directory):
        for file in files:
            old_path = os.path.join(root, file)
            new_name = rename_digits(file)
            new_path = os.path.join(temp_flat_dir, new_name)
            shutil.copy2(old_path, new_path)

    for file in sorted(os.listdir(temp_flat_dir)):
        path = os.path.join(temp_flat_dir, file)
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    combined.append(f"{file}:{line.strip()}")
        except Exception as e:
            print(f"Skipped file: {file}, Error: {e}")

    sorted_combined = "\n".join(sorted(combined))
    sha256_hash = hashlib.sha256(sorted_combined.encode("utf-8")).hexdigest()
    print(f"🔒 SHA256 Hash: {sha256_hash}")
    return sha256_hash


# ✅ Run it
if __name__ == "__main__":
    original_dir = r"C:\TDS-02\RollNo_23f3002675\Assignment_1\workdir\q-mv-rename-files"
    flat_dir = os.path.join(original_dir, "flattened")
    prepare_q16_hash(original_dir, flat_dir)
