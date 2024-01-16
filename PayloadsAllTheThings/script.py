import os

def change_extension(directory_path, old_extension, new_extension):
    for foldername, subfolders, filenames in os.walk(directory_path):
        for filename in filenames:
            if filename.endswith(old_extension):
                file_path = os.path.join(foldername, filename)
                new_file_path = os.path.splitext(file_path)[0] + new_extension
                os.rename(file_path, new_file_path)
                print(f'Renamed: {file_path} to {new_file_path}')

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    old_extension = ".txt"
    new_extension = ".md"
    
    change_extension(directory_path, old_extension, new_extension)
