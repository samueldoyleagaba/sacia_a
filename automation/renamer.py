import os

def batch_rename(path, prefix):
    if not os.path.exists(path):
        print("❌ Folder not found")
        return

    files = os.listdir(path)
    count = 1

    for file in files:
        old_path = os.path.join(path, file)
        if os.path.isfile(old_path):
            ext = os.path.splitext(file)[1]
            new_name = f"{prefix}_{count}{ext}"
            new_path = os.path.join(path, new_name)
            os.rename(old_path, new_path)
            print(f"✔ Renamed {file} → {new_name}")
            count += 1
