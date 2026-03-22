# AutoReconX

AutoReconX is a Python-based automated reconnaissance tool developed for learning and basic penetration testing tasks. It performs network scanning, service enumeration, and generates both readable and encrypted reports.

## Features

- Multi-threaded TCP port scanning
- Network discovery using ARP scan
- OS detection using Nmap
- Service enumeration:
  - Web enumeration
  - SMB enumeration
  - SSH enumeration
- Automated report generation
- Encrypted result storage for security

## Project Structure

AutoReconX/
│
├── cli/
├── scanner/
├── enumeration/
├── reporting/
├── crypto/


## Requirements

- Python 3.x
- Nmap installed on your system
- Required Python library:



pip install cryptography

## Usage

Run the tool using:

python cli.py <target_ip>

Example:

python cli.py 192.168.1.1



## Command Options

- -p / --ports → Specify port range (default: 1-2000)
- --web → Run web enumeration
- --smb → Run SMB enumeration
- --ssh → Run SSH enumeration
- --os → Detect operating system
- --arp → Perform network discovery
- -o / --output → Save report file



Example with options:

python cli.py 192.168.1.1 -p 1-2000 --web --smb --ssh --os -o report.txt


## Interactive Mode

If no target is provided, the tool runs in interactive mode:

python cli.py

The program will ask for input step-by-step.


## Output

The tool generates:

- A human-readable report file (.txt)
- An encrypted JSON file for secure storage


## Disclaimer

This project is created for educational purposes only.  
Do not use this tool on networks without proper authorization.

## Acknowledgment

Some parts of this project were developed with the assistance of AI tools for learning and guidance.

## Author

Rahul Yadav


