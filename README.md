# Python Port Scanner

A simple TCP port scanner built with Python’s `socket` module.

## Features

* Accepts an IP address or hostname
* Scans ports `1–100`
* Displays open ports
* Uses a timeout to avoid long delays

## Usage

```bash
python3 port_scanner.py
```

Example:

```text
Enter target IP or hostname: 127.0.0.1
Scanning 127.0.0.1...

[OPEN] Port 22
[OPEN] Port 80
```

## Requirements

* Python 3
* No external libraries required

## Disclaimer

For educational purposes only. Use this tool only on systems you own or have permission to test.
