# | hatcherdc | laptop cleanup | /cleanup.py |
import os
import subprocess

def delete_temp_files():
    files_deleted = 0
    temp_folder = os.environ.get('TEMP')
    for root, dirs, files in os.walk(temp_folder):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                files_deleted += 1
                print(f"Deleted:  {file_path}")
            except Exception as e:
                print(f"Failed to delete:  {file_path} ({str(e)})")
    return files_deleted

def delete_empty_directories():
    dirs_deleted = 0
    root_folder = os.path.expanduser("~")
    for root, dirs, files in os.walk(root_folder, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                os.rmdir(dir_path)
                dirs_deleted += 1
                print(f"Deleted:  {dir_path}")
            except Exception as e:
                print(f"Failed to delete:  {dir_path} ({str(e)})")
    return dirs_deleted

def print_num_results(files_deleted, dirs_deleted):
    print(f"\nFiles deleted: {files_deleted}\nEmpty Directories deleted: {dirs_deleted}\n")

def manage_startup_programs():
    startup_folder = os.path.join(os.environ.get('APPDATA'), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    startup_items = os.listdir(startup_folder)
    print("Startup Programs:")
    for item in startup_items:
        print(item)

def empty_recycle_bin():
    temp_folder = os.environ.get('TEMP')
    recycle_bin_path = os.path.join(temp_folder, "..",  "Recycle.Bin")
    try:
        subprocess.run(['cmd', '/c', 'rd', '/s', '/q', recycle_bin_path], check=True)
        print("Emptied the recycling bin!")
    except subprocess.CalledProcessError as e:
        stderr = e.stderr
        error_msg = stderr.decode() if stderr is not None else "Unknown Error"
        print(f"Failed to empty recycle bin ({error_msg})")

def driver():
    files_deleted = delete_temp_files()
    dirs_deleted = delete_empty_directories()
    print_num_results(files_deleted, dirs_deleted)
    manage_startup_programs()
    empty_recycle_bin()

if __name__ == "__main__":
    driver()