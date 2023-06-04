# **File and Directory Cleanup Script**

This script performs cleanup operations to remove temporary files and directories from the system.

---

## **Getting Started:**


### Prerequisites

- Python 3.x

---
### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
2. pip install psutil

---
### **Usage**

1.  Open a terminal or command prompt
2.  Navigate to the project directory.
3.  Run the cleanup script:
    > python cleanup_script.py
4.  The script will perform cleanup operations on temporary files and directories.
5.  After the cleanup is completed, a PC health check will be performed, displaying CPU, memory, and disk usage information.

---
### **Customization**
You can customize the script by modifying the following parameters:

* `LOG_FOLDER`: Specifies the folder where the log files will be stored.
   > Feel free to make changes to the script to fit your specific requirements.

---
### **Logs**
The cleanup script generates the following log files in the specified **`LOG_FOLDER`**:

* `cleanup_log.txt`: Log file for successful file and directory deletions.
* `failed_delete_log.txt`: Log file for failed file and directory deletions.

---
### **License**
This project is licensed under the MIT License - see the **[LICENSE](https://www.example.com)** file for details.

---