import psutil
import os
import time

def stop_charging():
    # For Windows, you might need to invoke powercfg to disable charging.
    # For Linux, stopping charging programmatically might not be possible directly via script. 
    # It's system-specific.
    
    if os.name == 'nt':  # Windows
        os.system('powercfg /batteryreport')
    elif os.name == 'posix':  # Linux
        print("Stopping charging in Linux isn't straightforward via script.")
        # Some laptops may allow you to control charging behavior through BIOS/UEFI settings or third-party software. Check first

def monitor_battery():
    while True:
        battery = psutil.sensors_battery()
        if battery.power_plugged and battery.percent == 100:
            print("Battery is at 100%. Stopping charging...")
            stop_charging()
            break
        else:
            print(f"Battery: {battery.percent}% - Charging: {'Yes' if battery.power_plugged else 'No'}")
            time.sleep(10)  # check every 10 seconds

if __name__ == "__main__":
    monitor_battery()
