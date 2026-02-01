def explain(task):
    explanations = {
        "organize": [
            "1. Read all files in a folder",
            "2. Check each file's extension",
            "3. Match extension to category",
            "4. Create folders if missing",
            "5. Move file automatically"
        ],
        "rename": [
            "1. Read file list",
            "2. Generate new names using a counter",
            "3. Rename files automatically"
        ]
    }

    if task in explanations:
        print("\n🧠 Automation Logic:")
        for step in explanations[task]:
            print(step)
    else:
        print("No explanation available")
