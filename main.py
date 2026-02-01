from automation.organizer import organize_folder
from automation.renamer import batch_rename
from learning.explain import explain

print("""
SACIA_A – Student Automation & Coding Intelligent Assistant
-----------------------------------------------------------
1. Organize Files
2. Batch Rename Files
3. Learn How Automation Works
4. Exit
""")

choice = input("Select an option: ")

if choice == "1":
    path = input("Enter folder path: ")
    organize_folder(path)
    explain("organize")

elif choice == "2":
    path = input("Enter folder path: ")
    prefix = input("Enter filename prefix: ")
    batch_rename(path, prefix)
    explain("rename")

elif choice == "3":
    task = input("Enter task (organize/rename): ")
    explain(task)

else:
    print("Goodbye 👋")
