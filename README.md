Task Automation with Python

## 📌 Project Overview

This project is a simple Python automation tool that organizes JPG files automatically. It finds all `.jpg` files from a source folder and moves them to a destination folder.

## 🎯 Objective

To automate a repetitive file management task using Python and reduce manual effort.

## 🛠️ Technologies Used

* Python
* `os` module
* `shutil` module

## ⚙️ How It Works

1. The program checks the source folder.
2. It identifies files with the `.jpg` extension.
3. It creates the destination folder if it does not exist.
4. It automatically moves the JPG files to the destination folder.
5. It displays the files moved and the total count.

## 📂 Project Structure

```text
CodeAlpha-Task-Automation/
│
├── task_automation.py
├── source_folder/
├── destination_folder/
└── README.md
```

## ▶️ How to Run

Place JPG files inside the `source_folder` and run:

```bash
python task_automation.py
```

The JPG files will be automatically moved to the `destination_folder`.

## 💡 Example

**Before:**

```text
source_folder/
├── image1.jpg
├── image2.jpg
└── notes.txt
```

**After:**

```text
source_folder/
└── notes.txt

destination_folder/
├── image1.jpg
└── image2.jpg
```

## 👩‍💻 Author

**Bhoomika H S**
