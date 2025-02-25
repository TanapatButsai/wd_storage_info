# Storage Device Information CLI

## 📌 Overview

This project is a **command-line application** that retrieves and displays storage device details, including:

- Path to the device
- Total capacity
- Unused capacity remaining

The program is designed to run on **Ubuntu 24.04** inside a **Docker container**.

## 🚀 Build and Run Instructions

### **1. Dependencies**

Ensure that you have **Docker installed** on your system. You can verify by running:

```bash
docker --version
```

If Docker is not installed, follow the official installation guide: [Docker Installation](https://docs.docker.com/get-docker/).

### **2. Clone the Repository**

```bash
git clone <repository_url>
cd wd_storage_info
```

### **3. Build the Docker Image**

```bash
docker build -t wd_storage_info .
```

### **4. Run the Application in a Docker Container**

```bash
docker run --rm --privileged wd_storage_info
```

If you want the container to access the **host system’s storage**, run:

```bash
docker run --rm --privileged -v /:/mnt wd_storage_info
```

## 📝 Programming & Testing Approach

This project follows a **modular approach** ensuring smooth execution inside a **Docker container running Ubuntu 24.04**. The script:

1. **Executes ****`df -h`** to retrieve storage details in a Linux environment.
2. **Parses the output** to extract:
   - Storage device path
   - Total capacity
   - Available space
3. **Filters out virtual filesystems** (e.g., Docker overlay volumes) to ensure accurate disk information.

The script was tested inside:

- **Ubuntu 24.04 Docker container ✅**
- **With ****`--privileged`**** mode enabled for full storage access ✅**

## 📂 Project Structure

```
wd_storage_info/
│── wd_storage_info.py   # Main script
│── Dockerfile           # Docker setup
│── README.md            # Project documentation
```

## 🔹 Notes

- The script must be executed **inside a Docker container running Ubuntu 24.04**.
- Ensure **`--privileged`**** mode** is used for proper storage detection.
- If running in a macOS or Windows environment, use the Docker container as instructed above.

## 🏁 Conclusion

This project efficiently retrieves storage device details while running inside an **Ubuntu 24.04 Docker container**, ensuring a lightweight, portable, and scalable approach to disk management.

