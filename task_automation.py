import os
import shutil


def organize_jpg_files(source_folder, destination_folder):
    """
    Moves all JPG/JPEG files from the source folder
    to the destination folder.
    """

    if not os.path.exists(source_folder):
        return {
            "success": False,
            "message": "Source folder does not exist.",
            "moved_files": []
        }

    os.makedirs(destination_folder, exist_ok=True)

    moved_files = []

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        if (
            os.path.isfile(source_path)
            and filename.lower().endswith((".jpg", ".jpeg"))
        ):
            destination_path = os.path.join(
                destination_folder,
                filename
            )

            # Avoid overwriting an existing file
            if os.path.exists(destination_path):
                name, extension = os.path.splitext(filename)
                counter = 1

                while os.path.exists(destination_path):
                    new_filename = f"{name}_{counter}{extension}"
                    destination_path = os.path.join(
                        destination_folder,
                        new_filename
                    )
                    counter += 1

            shutil.move(source_path, destination_path)
            moved_files.append(os.path.basename(destination_path))

    return {
        "success": True,
        "message": f"{len(moved_files)} JPG file(s) moved successfully.",
        "moved_files": moved_files
    }