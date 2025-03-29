import zipfile
import os
from datetime import datetime, timezone, timedelta

# === CONFIG ===
zip_path = r"C:\TDS-02\RollNo_23f3002675\Assignment_1\workdir\q-list-files-attributes.zip"
extract_to = r"C:\TDS-02\RollNo_23f3002675\Assignment_1\workdir\q-list-files-attributes"
threshold_size = 693  # bytes

# IST timezone offset
ist_offset = timedelta(hours=5, minutes=30)
ist_cutoff = datetime(2004, 9, 22, 4, 0, 0, tzinfo=timezone(ist_offset))


def extract_zip_preserve_timestamp(zip_path, extract_to):
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    with zipfile.ZipFile(zip_path, 'r') as zf:
        for zipinfo in zf.infolist():
            zf.extract(zipinfo, extract_to)
            extracted_path = os.path.join(extract_to, zipinfo.filename)

            # Reconstruct timestamp from zip metadata
            dt = datetime(*zipinfo.date_time)
            timestamp = dt.timestamp()
            try:
                os.utime(extracted_path, (timestamp, timestamp))
            except Exception as e:
                print(f"⚠ Could not update time for {extracted_path}: {e}")


def compute_total_size(directory):
    total = 0
    for root, _, files in os.walk(directory):
        for file in files:
            fpath = os.path.join(root, file)
            stat = os.stat(fpath)
            size = stat.st_size
            mtime = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).astimezone(timezone(ist_offset))

            if size >= threshold_size and mtime >= ist_cutoff:
                print(f"✔ {file} | Size: {size} | Modified: {mtime}")
                total += size

    return total


# === RUN ===
extract_zip_preserve_timestamp(zip_path, extract_to)
total_size = compute_total_size(extract_to)
print(f"\n📊 Total size of matching files: {total_size} bytes")
