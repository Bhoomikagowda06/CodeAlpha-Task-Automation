# CodeAlpha Task Automation

A simple **Python and Flask-based task automation website** that automatically identifies and moves JPG/JPEG files from a source folder to a destination folder.

## 🚀 Features

* Automatically detects `.jpg` and `.jpeg` files
* Moves files from the source folder to the destination folder
* Prevents overwriting existing files
* Displays the number of files processed
* Simple and clean web interface
* Built with Python and Flask

## 🛠️ Technologies Used

* Python
* Flask
* HTML
* CSS
* JavaScript
* OS and Shutil Python modules

## 📂 Project Structure

```text
CodeAlpha-Task-Automation/
│
├── app.py
├── task_automation.py
├── requirements.txt
│
├── source_folder/
├── destination_folder/
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

## ⚙️ How It Works

1. JPG/JPEG files are placed inside the `source_folder`.
2. The Flask website provides a **Run Automation** button.
3. Python checks the source folder for JPG/JPEG files.
4. Matching files are moved to the `destination_folder`.
5. The website displays the automation result and file count.

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/Bhoomikagowda06/CodeAlpha-Task-Automation.git
```

Go to the project folder:

```bash
cd CodeAlpha-Task-Automation
```

Install the required package:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python app.py
```

Open the website in your browser:

```text
http://127.0.0.1:5000
```

## 🎯 Purpose

This project demonstrates how Python can be used to automate repetitive file-management tasks through a simple web interface.

## 👩‍💻 Developed By

**Bhoomika H S**

CodeAlpha Internship – Task 1

