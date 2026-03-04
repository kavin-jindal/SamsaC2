  # SamsaC2 - Discord Command & Control Framework
  
  A Discord-based Command and Control (C2) framework for remote system management and security research. This project demonstrates advanced command execution, system manipulation, and remote administration capabilities through Discord bot integration.
  
  > **⚠️ DISCLAIMER**: This project is for educational and authorized security testing purposes only. Unauthorized access to computer systems is illegal. Use only on systems you own or have explicit permission to test.
  
  ## Table of Contents
  
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Quick Start](#quick-start)
  - [Troubleshooting](#troubleshooting)
  - [License](#license)
  - [Contributing](#contributing)
  - [Disclaimer](#disclaimer)
  - [Contact & Support](#contact--support)
  - [About the Developers](#about-the-developers)
  
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
  ### Discord Bot Setup

Before using the compiler, you need to set up a Discord bot and obtain necessary credentials:

#### Step 1: Create a Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **"New Application"** and give it a name
3. Navigate to the **"Bot"** section and click **"Add Bot"**
4. Under **TOKEN**, click **"Copy"** to copy your bot token (keep this secret!)

#### Step 2: Configure Bot Intents

1. In the Bot section, scroll to **"INTENTS"**
2. Enable the following intents:
   - **Message Content Intent** (required for command reading)
   - **Server Members Intent** (for member management)
   - **Guilds** (for server access)

#### Step 3: Set Bot Permissions

1. Navigate to **"OAuth2"** → **"URL Generator"**
2. Under **"SCOPES"**, select:
   - `bot`
3. Under **"PERMISSIONS"**, select:
   - **Administrator** (to ensure full access)
4. Copy the generated URL and use it to invite the bot to your server

#### Step 4: Compiler Configuration

When running `compiler.py`, you will be prompted to enter:

- **Bot Token**: Paste the token from your Discord bot (obtained from Developer Portal)
- **Prefix**: Choose a command prefix (e.g., `!`, `$`, `.`) for executing commands
- **Executable Name**: Name for the compiled executable file (e.g., `samsac2`)
- **Server Name**: Name of the Discord server where the C2 will operate
- **Encryption Key**: A Fernet key for encrypting/decrypting files

#### Generating a Fernet Encryption Key

To generate a Fernet key, run:

```python
from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key.decode())
```

Copy the generated key and paste it when prompted in the compiler.

  ## Setup 
  
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
  
  
  ## Future updates
  - [ ] Keylogger integration
  - [ ] Webcam and microphone surveilance
  - [ ] Display manipulation
  
  
  
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
  
  **LEGAL WARNING**: This software is for authorized security testing and educational purposes only. Unauthorized access to computer systems is     illegal under the Computer Fraud and Abuse Act (18 U.S.C. § 1030) and similar international laws. The author is not responsible for misuse or damages caused by this software.
  
  ## About the Developers

  ### Avyukt Security
    
  - [**Medium**](https://medium.com/@avyuktsec)
  - [**LinkedIn**](https://www.linkedin.com/company/avyukt-security/)
  
  
  ## Contact & Support
  
  For questions or issues, open a GitHub issue or submit a pull request.
  
  ---
  
  **Last Updated**: March 4, 2026  
  **Status**: Active Development  
  
