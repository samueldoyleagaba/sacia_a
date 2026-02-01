
import os
import shutil

FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Code": [".py", ".c", ".cpp", ".java"],
    "Archives": [".zip", ".rar"]
}

def organize_folder(path):
    if not os.path.exists(path):
        print("❌ Folder not found")
        return

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()

            for folder, extensions in FILE_TYPES.items():
                if ext in extensions:
                    target_dir = os.path.join(path, folder)
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.move(file_path, target_dir)
                    print(f"✔ Moved {filename} → {folder}")
                    break
