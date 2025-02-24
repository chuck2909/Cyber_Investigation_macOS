import os
import re
import time
import subprocess
import requests
from collections import Counter

# Function to extract active connections
def get_active_connections():
    result = subprocess.run(["netstat", "-an"], capture_output=True, text=True)
    return result.stdout

# Function to extract external IPs
def extract_ips(log_data):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ips = re.findall(ip_pattern, log_data)
    # Filter out local IPs
    external_ips = [ip for ip in ips if not ip.startswith(("192.168", "10.", "127.", "0."))]
    return external_ips

# Function to get WHOIS information
def get_whois(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        return f"{ip} - {response.get('country', 'Unknown')} - {response.get('isp', 'Unknown')}"
    except:
        return f"{ip} - WHOIS Lookup Failed"

#  Function to analyze and log findings
def analyze_network():
    print("\n🔍 Scanning active connections...\n")
    log_data = get_active_connections()
    external_ips = extract_ips(log_data)
    
    if not external_ips:
        print(" No external connections detected.\n")
        return
    
    # Count occurrences of each IP
    ip_counts = Counter(external_ips)

    # Save results to a log file
    log_file = "network_analysis.log"
    with open(log_file, "w") as f:
        f.write("\n Network Threat Analysis\n\n")
        f.write("External IPs Found:\n")
        for ip, count in ip_counts.most_common(10):
            f.write(f"{ip} - Seen {count} times\n")

        f.write("\n WHOIS Lookups:\n")
        for ip in external_ips[:5]:  # Limit WHOIS lookups for speed
            whois_info = get_whois(ip)
            f.write(whois_info + "\n")
            print(whois_info)  # Print to console as well
    
    print(f"\n Analysis complete! Results saved to: {log_file}\n")

# Run the analysis every 60 seconds (adjust as needed)
if __name__ == "__main__":
    while True:
        analyze_network()
        time.sleep(60)  # Adjust the interval as needed
 
