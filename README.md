# SamsaC2 - Discord Command & Control Framework

A Discord-based Command and Control (C2) framework for remote system management and security research. This project demonstrates advanced command execution, system manipulation, and remote administration capabilities through Discord bot integration.

> **⚠️ DISCLAIMER**: This project is for educational and authorized security testing purposes only. Unauthorized access to computer systems is illegal. Use only on systems you own or have explicit permission to test.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Core Functions Reference](#core-functions-reference)
- [Development Roadmap](#development-roadmap)
- [Security Considerations](#security-considerations)
- [Troubleshooting](#troubleshooting)

## Features

### Core Capabilities

- **Remote Shell Execution** - Execute Windows CMD commands remotely
- **PowerShell Integration** - Run PowerShell scripts and commands
- **Process Management** - List and terminate running tasks
- **File Transfer** - Upload/download files via Discord
- **System Information** - Retrieve system details and IP information
- **Screenshot Capture** - Take screenshots of target system
- **Clipboard Access** - Read and manipulate system clipboard
- **Encryption/Decryption** - Secure file operations using Fernet encryption

### Advanced Features

- **Persistence** - Automatic startup registry entries
- **Long Output Handling** - Store large command outputs as files
- **IP Detection** - Public IP address retrieval
- **Obfuscation** - PyInstaller executable compilation
- **Session Management** - Maintain multiple active remote sessions


## Prerequisites

- **Python 3.8+**
- **Windows OS** (primary target)
- **Administrator privileges** (for system-level operations)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/SamsaC2.git
cd SamsaC2
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### Dependencies Overview

| Package | Purpose |
|---------|---------|
| `nextcord` | Discord bot framework |
| `pyscreeze` | Screenshot capture |
| `psutil` | Process management |
| `pyautogui` | Automated GUI control |
| `requests` | HTTP requests |
| `cryptography` | Fernet encryption |
| `pillow` | Image manipulation |
| `pyinstaller` | Executable compilation |



## Quick Start

### Step 1: Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

### Step 2: Run the Compiler

Use the compiler script to generate scripts and their executable versions:

```bash
python compiler.py
```

This will:
- Generate the C2 script
- Generate compiled executables using PyInstaller
- Place outputs in the `dist/` directory

### Step 3: Use Generated Executable

Locate your compiled executable in the `dist/` folder. Run it as a standalone program without requiring Python installation on target systems.


### Discord Commands

For users running a bot instance, the following commands are available
(using the configured prefix):

| Command | Description |
|---------|-------------|
| `help` | Show help menu |
| `cmd <command>` | Execute a shell command |
| `cd <path>` | Change directory |
| `ps <cmd>` | Run PowerShell command |
| `tasklist` | List running processes |
| `stoptask <name>` | Kill a process by name |
| `ss` | Take a screenshot |
| `send` | Upload a file to the client |
| `recv <path>` | Download a file from the client |
| `encrypt <file>` | Encrypt a file |
| `decrypt <file>` | Decrypt an encrypted file |
| `hide <file/dir> <path>` | Hide a file or directory |
| `unhide <file/dir> <path>` | Unhide a file or directory |
| `press <key>` | Simulate a key press |
| `type <string>` | Type text at the cursor |
| `clipboard` | Read clipboard contents |
| `web <url>` | Open a URL in default browser |
| `wifip` | Retrieve stored Wi‑Fi passwords |
| `quit` | Exit the session |


## Development Roadmap

### Short Term



### Long Term




## Security Considerations

### Encryption

The `samsac2.py` module uses Fernet (AES-128 CBC) for file encryption:

```python
key = b'-XXPx0gJig0dDea3XaJO0MDJJO4BGc3xg7_MDY4wetk='
```

**⚠️ CRITICAL**: The encryption key is hardcoded in the source. In production:
- Generate a new key: `from cryptography.fernet import Fernet; Fernet.generate_key()`
- Store keys securely (environment variables, key management services)
- Never commit keys to version control



## Troubleshooting

### Import Errors

Ensure dependencies are installed:
```bash
pip install -r requirements.txt
```

### Encryption/Decryption Issues

- Verify the encryption key matches between encryption and decryption operations
- Check file permissions (file must be readable/writable)
- Ensure sufficient disk space for large file operations

### Executable Build Failures

- Check PyInstaller is installed: `pip install pyinstaller`
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check for hidden import warnings in compiler output

## Code Examples

### Using samsac2.py Core Module

Execute system commands:

```python
import samsac2

# Run shell command
output = samsac2.cmd('whoami')
print(output)  # Output: ```username```

# Change directory
samsac2.cd('C:\\Windows')
```

### File Encryption

```python
import samsac2

# Encrypt a sensitive file
samsac2.encrypt('sensitive_data.txt')

# Later, decrypt it
samsac2.decrypt('sensitive_data.txt')
```

### Clipboard Operations

```python
import samsac2

# Read clipboard content
text = samsac2.clipboard()
print(f"Clipboard: {text}")
```

### Taking Screenshots

```python
import samsac2

# Screenshot saved to temp directory
samsac2.screenshot()
# File saved at: C:\Users\[user]\AppData\Local\Temp\ss1.png
```



## License

This project is provided as-is for educational purposes. Modify and use at your own risk.

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Submit a pull request

## Disclaimer

**LEGAL WARNING**: This software is for authorized security testing and educational purposes only. Unauthorized access to computer systems is illegal under the Computer Fraud and Abuse Act (18 U.S.C. § 1030) and similar international laws. The author is not responsible for misuse or damages caused by this software.

## Contact & Support

For questions or issues, open a GitHub issue or submit a pull request.

---

**Last Updated**: March 2, 2026  
**Status**: Active Development  
**Current Focus**: Core Utility Module & Build System  
**Version**: 2.1 (SamsaC2 - Refactored)
