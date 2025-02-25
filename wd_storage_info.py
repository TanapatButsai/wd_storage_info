import os
import platform
import subprocess
import json

def get_storage_info():
    system = platform.system()

    if system == "Linux":
        return get_linux_storage_info()
    elif system == "Windows":
        return get_windows_storage_info()
    elif system == "Darwin":  # macOS is identified as "Darwin"
        return get_macos_storage_info()
    else:
        print("Unsupported OS")
        return []

def get_linux_storage_info():
    try:
        # Use 'df -h /mnt' to get the real macOS storage
        result = subprocess.run(["df", "-h", "/mnt"], capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split("\n")[1:]  # Skip header line
        
        devices = []
        for line in lines:
            parts = line.split()
            if len(parts) < 6:
                continue  # Skip malformed lines
            
            filesystem, size, used, available, percent, mountpoint = parts
            
            devices.append({
                "Path": filesystem,
                "Total Capacity": size,
                "Unused Capacity": available
            })
        
        return devices
    except Exception as e:
        print(f"Error: {e}")
        return []

def get_windows_storage_info():
    try:
        result = subprocess.run(["wmic", "logicaldisk", "get", "DeviceID,Size,FreeSpace"], capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split("\n")[1:]  # Skip header
        
        devices = []
        for line in lines:
            parts = line.split()
            if len(parts) < 2:
                continue  # Skip malformed lines
            
            drive = parts[0]
            total_size = int(parts[1]) / (1024 ** 3) if len(parts) > 1 else "Unknown"
            free_space = int(parts[2]) / (1024 ** 3) if len(parts) > 2 else "Unknown"
            
            devices.append({
                "Path": drive,
                "Total Capacity": f"{total_size:.2f} GB",
                "Unused Capacity": f"{free_space:.2f} GB"
            })
        
        return devices
    except Exception as e:
        print(f"Error: {e}")
        return []

def get_macos_storage_info():
    try:
        result = subprocess.run(["df", "-h"], capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split("\n")[1:]  # Skip header line
        
        devices = []
        for line in lines:
            parts = line.split()
            if len(parts) < 6:
                continue  # Skip malformed lines
            
            filesystem, size, used, available, percent, mountpoint = parts
            devices.append({
                "Path": filesystem,
                "Total Capacity": size,
                "Unused Capacity": available
            })
        
        return devices
    except Exception as e:
        print(f"Error: {e}")
        return []

def print_storage_info():
    devices = get_storage_info()
    
    if not devices:
        print("No storage devices found or error retrieving data.")
        return
    
    print("Storage Device Information:")
    for device in devices:
        print(f"Path: {device['Path']}")
        print(f"Total Capacity: {device['Total Capacity']}")
        print(f"Unused Capacity: {device['Unused Capacity']}")
        print("-" * 40)

if __name__ == "__main__":
    print_storage_info()
