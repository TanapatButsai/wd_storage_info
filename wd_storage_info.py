import os
import subprocess

def get_storage_info():
    try:
        # Run df -h command to get storage device details
        result = subprocess.run(["df", "-h"], capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split("\n")[1:]  # Skip header line
        
        devices = []
        ignore_list = ["tmpfs", "overlay", "shm"]  # Ignore virtual filesystems
        
        for line in lines:
            parts = line.split()
            if len(parts) < 6:
                continue  # Skip malformed lines
            
            filesystem, size, used, available, percent, mountpoint = parts
            
            # Filter out virtual filesystems
            if any(ignore in filesystem for ignore in ignore_list):
                continue
            
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
