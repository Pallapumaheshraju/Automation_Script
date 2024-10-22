import os
import shutil

def organize_files(directory):
    # Create a list of file extensions to organize
    extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.pptx'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Audios': ['.mp3', '.wav'],
    }

    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        print(filename)
        file_ext = os.path.splitext(filename)[1].lower()
        for folder_name, ext_list in extensions.items():
            if file_ext in ext_list:
                # Create folder if it doesn't exist
                folder_path = os.path.join(directory, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                # Move file to the corresponding folder
                shutil.move(os.path.join(directory, filename), os.path.join(folder_path, filename))
                print(f'Moved: {filename} to {folder_name}')
                break

def copy_files_to_folders(directory):
    # Create a list of file extensions to organize
    extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.pptx'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Audios': ['.mp3', '.wav'],
    }

    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        file_ext = os.path.splitext(filename)[1].lower()
        for folder_name, ext_list in extensions.items():
            if file_ext in ext_list:
                # Create folder if it doesn't exist
                folder_path = os.path.join(directory, os.path.join('Organized_Files', folder_name))
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                # Copy file to the corresponding folder
                shutil.copy2(os.path.join(directory, filename), os.path.join(folder_path, filename))
                print(f'Copied: {filename} to {folder_name}')
                break

print("Started..")
copy_files_to_folders('Files')
# organize_files('Files')