import os
import shutil
import datetime
import sys
import itertools
import tempfile

# ANSI escape sequences for text formatting
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BOLD = "\033[1m"
RESET = "\033[0m"

LOG_FOLDER = "cleanup_logs"

def cleanup_temporary_files():
    """
    Cleans up temporary files from the system's temporary folder.
    """
    temp_folder = tempfile.gettempdir()
    log_file = os.path.join(LOG_FOLDER, "cleanup_log.txt")
    failed_log_file = os.path.join(LOG_FOLDER, "failed_delete_log.txt")

    # Create or open the log file in append mode
    os.makedirs(LOG_FOLDER, exist_ok=True)

    with open(log_file, 'a') as f:
        with open(failed_log_file, 'a') as d:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[[ Cleanup Files Log ]] - {current_time}\n\n")
            d.write(f"\n[[ Failed to Delete Files Log ]] - {current_time}\n\n")

            deleted_files = 0
            total_files = 0

            # Count total number of files
            for root, dirs, files in os.walk(temp_folder):
                total_files += len(files)

            print("Cleanup in progress - Files...")
            animation = itertools.cycle(["|", "/", "-", "\\"])

            # Delete each file and update progress animation
            for root, dirs, files in os.walk(temp_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        os.remove(file_path)
                        f.write(f"Deleted File: {file_path}\n")
                        deleted_files += 1
                    except Exception as e:
                        d.write(f"Failed to delete File: {file_path} ({str(e)})\n")

                    # Update the progress animation
                    sys.stdout.write(f"\r{GREEN}{next(animation)}{RESET}")
                    sys.stdout.flush()

            # Update security on log files
            os.chmod(log_file, 0o600)
            os.chmod(failed_log_file, 0o600)

            sys.stdout.write("\r")
            print("File cleanup completed.")
            print(f"{BOLD}Deleted Files: {deleted_files}{RESET}\n")


def cleanup_temporary_directories():
    """
    Cleans up temporary directories from the system's temporary folder.
    """
    temp_folder = tempfile.gettempdir()
    log_file = os.path.join(LOG_FOLDER, "cleanup_log.txt")
    failed_log_file = os.path.join(LOG_FOLDER, "failed_delete_log.txt")

    # Create or open the log file in append mode
    with open(log_file, 'a') as f:
        with open(failed_log_file, 'a') as d:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[[ Cleanup Directories Log ]] - {current_time}\n\n")
            d.write(f"\n[[ Failed to Delete Directories Log ]] - {current_time}\n\n")
            deleted_dirs = 0

            print("Cleanup in progress - Directories...")
            animation = itertools.cycle(["|", "/", "-", "\\"])

            # Delete each directory and update progress animation
            for root, dirs, files in os.walk(temp_folder, topdown=False):
                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    try:
                        os.rmdir(dir_path)
                        f.write(f"Deleted Directory: {dir_path}\n")
                        deleted_dirs += 1
                    except Exception as e:
                        d.write(f"Failed to delete Directory: {dir_path} ({str(e)})\n")

                    # Update the progress animation
                    sys.stdout.write(f"\r{GREEN}{next(animation)}{RESET}")
                    sys.stdout.flush()

            # Update security on log files
            os.chmod(log_file, 0o600)
            os.chmod(failed_log_file, 0o600)

            sys.stdout.write("\r")
            print("Directory cleanup completed.")
            print(f"{BOLD}Deleted Directories: {deleted_dirs}{RESET}")


def cleanup_temporary():
    """
    Performs cleanup of temporary files and directories.
    """
    cleanup_temporary_files()
    cleanup_temporary_directories()
    os.chmod(LOG_FOLDER, 0o600)


def pc_health_check():
    """
    Performs a health check of the PC.
    """
    # Health check implementation (CPU, memory, disk usage)
    pass


if __name__ == "__main__":
    cleanup_temporary()
    pc_health_check()