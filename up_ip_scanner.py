import subprocess

def main():
    # Get the subnet information from the user
    subnet = input("Please enter the subnet you want to discover up IPs for (e.g., 192.168.1.0/24): ")

    # Generate the file name based on the subnet
    subnet_filename = subnet.replace("/", "-") + "-up-list.txt"

    # Run the Nmap command
    print(f"Scanning for up IPs on {subnet}... Please wait.")
    nmap_command = f"nmap -sn {subnet} -oG -"
    result = subprocess.run(nmap_command, shell=True, capture_output=True, text=True)

    # Process the results to list up IPs
    up_ips = []
    for line in result.stdout.splitlines():
        if "Up" in line:
            ip = line.split()[1]
            up_ips.append(ip)

    # Save the up IPs to a file
    with open(subnet_filename, 'w') as file:
        for ip in up_ips:
            file.write(ip + "\n")

    print(f"Scan complete! Up IPs have been saved to {subnet_filename}.")

if __name__ == "__main__":
    main()