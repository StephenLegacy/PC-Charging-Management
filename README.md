

# Battery Monitoring Script for Stopping Charging at 100%

**Created By StephenLegacy**

This Python script monitors your computer's battery status and automatically stops charging once the battery reaches 100%. The script works on **Windows** and **Linux**, but note that stopping charging programmatically in Linux may not be straightforward. 

### Prerequisites

Before you start, make sure you have the following installed - Dwnload from the official websites
:

- **Python** (version 3.x)
- **pip** (Python's package installer)

### Dependencies

You need to install the `psutil` library, which provides access to battery information and other system-related functionalities.

To install the required dependency, run:

```bash
pip install psutil
```

### Script Overview

The script will:

1. Monitor the battery's charge percentage.
2. Check if the laptop is plugged in.
3. Stop charging when the battery reaches 100%.
4. Display the current charging status.

### How It Works

- The script periodically checks the battery's percentage and whether the laptop is plugged in.
- When the battery reaches 100%, the script triggers an action to stop charging.
- For **Windows**, it attempts to generate a battery report using `powercfg`.  
- For **Linux**, stopping charging programmatically might not be directly feasible without specific system utilities.

---

### How to Deploy and Run the Script

#### 1. Clone or Download the Script

Create a folder for the project and place the script `battery_monitor.py` in it.

```bash
mkdir battery-monitor
cd battery-monitor
```

You can download the script or copy-paste it directly into a file named `battery_monitor.py`.

#### 2. Install Dependencies

Make sure you have `psutil` installed, as it's required to fetch battery status.

Run the following command to install it:

```bash
pip install psutil
```

#### 3. Run the Script

After you've set up everything, run the script by executing:

```bash
python battery_monitor.py
```

The script will now monitor your battery, and when it hits 100%, it will attempt to stop charging based on your operating system.

---

### Platform-Specific Details

#### Windows

- On **Windows**, the script uses the `powercfg /batteryreport` command to create a battery report, though it doesn't directly stop charging. However, this may help gather information about your battery status.
  
- If you need better control over stopping charging on Windows, consider using third-party software (e.g., BatteryCare, or manufacturer-specific utilities like Dell Power Manager).

#### Linux

- **Linux** does not have a built-in method to stop charging via a Python script easily. You may need to rely on utilities like `tlp` or adjust settings in your system's BIOS/UEFI to set charging thresholds (e.g., stop charging after 80% or a similar threshold).
  
- This script provides a placeholder to print a message indicating stopping charging isn't directly feasible via Python on Linux.

---

### Troubleshooting

1. **Script not working as expected:**

   - Ensure you have `psutil` installed correctly.
   - For **Windows**: Make sure you are running the script with administrative privileges if needed for certain system commands.
   - For **Linux**: Ensure your system allows battery management via utilities or BIOS settings.

2. **Charging not stopping**:  
   Stopping charging is hardware-specific. On most systems, you need to rely on third-party software or BIOS/UEFI to manage charging behavior directly.

---

### Conclusion

This Python script is a useful way to monitor your battery status and stop charging when it reaches 100%. While **Windows** users can use the `powercfg` command for battery management, **Linux** users may need to explore third-party tools for better control over charging.

If you'd like to take further control over your battery's charging threshold, look into:
- **Windows**: Use software like **BatteryCare** or **Dell Power Manager**.
- **Linux**: Use **tlp** or system utilities to manage charging.

---

