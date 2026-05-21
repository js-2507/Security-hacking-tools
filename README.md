<h1>Security Tools</h1>

<h2>1. Simple Python Network Port Scanner</h2>

A lightweight, cross-platform Python CLI tool used to verify host availability and scan network ports. It uses standard library modules to ping a target host before scanning either a single port or a sequential range of TCP ports.

## Features

- **Host Verification:** Automatically pings the target IP address to check if it is reachable before running a scan.
- **Cross-Platform Support:** Dynamically adjusts ping flags depending on whether the host machine is running Windows, macOS, or Linux.
- **Flexible Scanning Modes:** 
  - Scan a specific single port.
  - Scan an entire custom range of ports.
- **Zero External Dependencies:** Built entirely with standard Python libraries (`socket`, `subprocess`, `platform`).
- **Graceful Error Handling:** Catches invalid user inputs and handles `KeyboardInterrupt` signals to exit smoothly.

### Prerequisites

- **Python 3.x** installed on your system.
- Network access to the target IP address.

### Installation

1. Clone or download this repository to your local machine.
2. Save the script as `PortScanner.py`.

### Usage

Run the script from your terminal or command prompt:

```bash
python PortScanner.py
