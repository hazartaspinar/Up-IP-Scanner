## Nmap Up IP Scanner

This Python script allows you to quickly discover and save the online (up) IP addresses within a specified subnet. By entering a subnet (e.g., `192.168.1.0/24`), the script uses Nmap to identify live hosts and automatically saves the results in a text file formatted as `subnet-up-list.txt`.

### Key Features:

- **Subnet Input:** The user specifies the subnet to scan.
- **Nmap Integration:** Utilizes Nmap for efficient host discovery.
- **Automatic File Naming:** Generates output file names based on the subnet provided.
- **Easy to Use:** Just run the script, enter the subnet, and get a list of online IPs.

### Example Use Case:

- **Network Administrators:** Quickly identify active devices in a subnet.
- **Security Professionals:** Pre-scan a network to find live hosts before deeper analysis.

## How to Use

1. **Install Nmap:** Make sure you have Nmap installed on your system. You can install it via the package manager of your operating system. For example:
   - **Debian/Ubuntu:** `sudo apt-get install nmap`
   - **CentOS/RHEL:** `sudo yum install nmap`
   - **macOS:** `brew install nmap`

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/hazartaspinar/up-ip-scanner
