import subprocess
import time
import re

# Define the log file path
LOG_FILE = "/var/log/auth.log"

# Function to get location information from IP address using geoiplookup
def get_location(ip_address):
    try:
        output = subprocess.check_output(["geoiplookup", ip_address]).decode("utf-8")
        location = re.search(r'GeoIP Country Edition: (.+)', output)
        if location:
            return location.group(1)
    except subprocess.CalledProcessError:
        pass
    return "Unknown"

# Function to monitor the log file for new invalid login attempts
def monitor_log():
    last_line = 0
    while True:
        try:
            with open(LOG_FILE, 'r') as file:
                file.seek(0, 2)
                file_size = file.tell()
                file.seek(last_line)

                for line in file:
                    last_line += len(line)
                    if "Invalid" in line:
                        ip_address = line.split()[-3]
                        location = get_location(ip_address)
                        print(f"[*] The Attacker's Country: {location} [IP ADDRESS: {ip_address}]")

                if last_line > file_size:
                    last_line = 0  # Reset the position if the file has been truncated
        except FileNotFoundError:
            print(f"Error: Log file '{LOG_FILE}' not found.")
            break
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(2)

if __name__ == "__main__":
    monitor_log()

