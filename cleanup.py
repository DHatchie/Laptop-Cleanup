import os
import shutil
import datetime
import sys
import itertools
import psutil

# ANSI escape sequences for text formatting
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BOLD = "\033[1m"
RESET = "\033[0m"

LOG_FOLDER = "cleanup_logs"

def cleanup_temporary_files():
    temp_folder = os.environ.get('TEMP')
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
            deleted_dirs = 0
            total_files = 0

            for root, dirs, files in os.walk(temp_folder):
                total_files += len(files)

            print("Cleanup in progress - Files...")
            animation = itertools.cycle(["|", "/", "-", "\\"])

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

            sys.stdout.write("\r")
            print("File cleanup completed.")
            print(f"{BOLD}Deleted Files: {deleted_files}{RESET}\n")


def cleanup_temporary_directories():
    temp_folder = os.environ.get('TEMP')
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

            for root, dirs, files in os.walk(temp_folder):
                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    try:
                        shutil.rmtree(dir_path)
                        f.write(f"Deleted Directory: {dir_path}\n")
                        deleted_dirs += 1
                    except Exception as e:
                        d.write(f"Failed to delete Directory: {dir_path} ({str(e)})\n")

                    # Update the progress animation
                    sys.stdout.write(f"\r{GREEN}{next(animation)}{RESET}")
                    sys.stdout.flush()

            sys.stdout.write("\r")
            print("Directory cleanup completed.")
            print(f"{BOLD}Deleted Directories: {deleted_dirs}{RESET}")


def cleanup_temporary():
    cleanup_temporary_files()
    cleanup_temporary_directories()


def pc_health_check():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage(os.getcwd()).percent

    print(f"\n{BOLD}PC Health Check:{RESET}")
    print(f"CPU Usage: {YELLOW}{cpu_usage}%{RESET}")
    print(f"Memory Usage: {YELLOW}{memory_usage}%{RESET}")
    print(f"Disk Usage: {YELLOW}{disk_usage}%{RESET}\n")


if __name__ == "__main__":
    cleanup_temporary()
    pc_health_check()