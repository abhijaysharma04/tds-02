import os
import re

directory = directory = r"C:\TDS-02\RollNo_23f3002675\Assignment_1\workdir\q-replace-across-files"

for filename in os.listdir(directory):
    path = os.path.join(directory, filename)
    if os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        updated = re.sub(r'iitm', 'IIT Madras', content, flags=re.IGNORECASE)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(updated)
