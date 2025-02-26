# Storage Device Information CLI

## 📌 Overview
This is a **command-line application** that retrieves and displays storage device details inside an **Ubuntu 24.04 Virtual Machine (VM)**. The program outputs:
- **Path to the storage device**
- **Total capacity**
- **Unused capacity remaining**

This project follows the requirement to run inside an **Ubuntu 24.04 VM** without relying on external packages not available in the default Ubuntu repository.

## 🚀 Build and Run Instructions

### **1. Prerequisites (Requirements Before Running the Project)**
Before running this project, make sure you have:
- **Ubuntu 24.04 installed** inside a Virtual Machine (VMware, VirtualBox, or WSL)
- **Python 3 installed** (Pre-installed in Ubuntu 24.04)
- **Git installed** (optional for cloning the repository)

To verify Python 3 is installed, run:
```bash
python3 --version
```

To install Git (if needed):
```bash
sudo apt update && sudo apt install -y git
```

### **2. Clone the Repository (Download the Project)**
```bash
git clone <repository_url>
cd wd_storage_info
```

### **3. Run the Application**
Execute the script using Python 3:
```bash
python3 storage_info_ubuntu.py
```

## 📝 My Approach to Programming & Testing
This project was designed with **simplicity and efficiency** in mind, making it easy to execute on any Ubuntu 24.04 system. The script:
1. **Uses the `df -h` command** to retrieve system storage details.
2. **Processes the output**, filtering out unneeded virtual filesystems (like `tmpfs`, `overlay`, and `shm`).
3. **Displays clean, user-friendly information**, including:
   - Storage device path
   - Total capacity
   - Available space

### **Testing Approach**
- The script was tested in an **Ubuntu 24.04 Virtual Machine (VM)** to ensure correct execution.
- Multiple storage devices were checked for accurate readings.
- Unnecessary virtual filesystems were filtered to improve data clarity.

## 📂 Project Structure
```
wd_storage_info/
│── storage_info_ubuntu.py   # Main script to retrieve storage details
│── README.md                # Documentation for the project
```

## 🔹 Notes (Things I Learned & Important Reminders)
- This project **must** be run inside a **VM running Ubuntu 24.04**.
- The script filters out virtual filesystems to ensure only real storage devices are displayed.
- If the output is missing expected storage devices, running `df -h` manually can help debug.

## 🏁 Conclusion
This project helped me understand how to interact with system storage inside an **Ubuntu VM**, process Linux system commands in Python, and present the data in a clear and structured format.



