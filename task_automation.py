import os
import shutil

# Define source and destination folders
source_folder = "source_folder"
destination_folder = "destination_folder"

# Check if source folder exists
if not os.path.exists(source_folder):
    print("Source folder does not exist.")
    exit()

# Create destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Count moved files
moved_files = 0

# Find and move JPG files
for file_name in os.listdir(source_folder):

    if file_name.lower().endswith(".jpg"):

        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        shutil.move(source_path, destination_path)

        print(f"Moved: {file_name}")
        moved_files += 1

# Display final result
print("\n--------------------------------")
print("Task Automation Completed!")
print(f"Total JPG files moved: {moved_files}")
print("--------------------------------")