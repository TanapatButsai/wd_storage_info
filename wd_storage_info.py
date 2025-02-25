import os
import subprocess
import json

def get_storage_info():
    try:
        # Run lsblk command to get storage device details in JSON format
        result = subprocess.run(["lsblk", "-J", "-o", "NAME,SIZE,MOUNTPOINT"], capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        
        devices = []
        for device in data.get("blockdevices", []):
            name = device.get("name", "Unknown")
            size = device.get("size", "Unknown")
            mountpoint = device.get("mountpoint", "Not Mounted")
            
            if mountpoint == "Not Mounted":
                free_space = "N/A"
            else:
                try:
                    statvfs = os.statvfs(mountpoint)
                    free_space = f"{(statvfs.f_bavail * statvfs.f_frsize) / (1024 ** 3):.2f} GB"
                except Exception:
                    free_space = "Error fetching"
            
            devices.append({
                "Path": f"/dev/{name}",
                "Total Capacity": size,
                "Unused Capacity": free_space
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
