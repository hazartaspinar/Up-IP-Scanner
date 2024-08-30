import subprocess

def get_subnet():
    """Prompt the user to enter a subnet."""
    return input("Please enter the subnet you want to discover up IPs for (e.g., 192.168.1.0/24): ")

def generate_filename(subnet):
    """Generate a filename based on the subnet."""
    return subnet.replace("/", "-") + "-up-list.txt"

def run_nmap_scan(subnet):
    """Run the Nmap command and return the output."""
    nmap_command = f"nmap -sn {subnet} -oG -"
    try:
        result = subprocess.run(nmap_command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running Nmap scan: {e}")
        return ""

def extract_up_ips(output):
    """Extract up IPs from the Nmap output."""
    up_ips = []
    for line in output.splitlines():
        if "Up" in line:
            ip = line.split()[1]
            up_ips.append(ip)
    return up_ips

def save_ips_to_file(filename, ips):
    """Save the list of IPs to a file."""
    with open(filename, 'w') as file:
        for ip in ips:
            file.write(ip + "\n")

def main():
    subnet = get_subnet()
    filename = generate_filename(subnet)
    
    print(f"Scanning for up IPs on {subnet}... Please wait.")
    nmap_output = run_nmap_scan(subnet)
    
    up_ips = extract_up_ips(nmap_output)
    save_ips_to_file(filename, up_ips)
    
    print(f"Scan complete! Up IPs have been saved to {filename}.")

if __name__ == "__main__":
    main()
