  # SamsaC2 - Discord Command & Control Framework  
  
  A Discord-based Command and Control (C2) framework for remote system management and security research. This project demonstrates advanced command execution, system manipulation, and remote administration capabilities through Discord bot integration.
  
  > **⚠️ DISCLAIMER**: This project is for educational and authorized security testing purposes only. Unauthorized access to computer systems is illegal. Use only on systems you own or have explicit permission to test.
  
  ## Table of Contents
  
  - [Features](#features)
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

- Run the compiler.py file using python3 compiler.py. Press Enter to initiate the process.

![img1](/images/1.png)

- Input all the details as asked

![img2](/images/2.png)

- Make sure to use the Discord server where the bot is invited and has the relevant permissions.
- Next, to generate the Fernet key, use the following script or use a third-party service like https://8gwifi.org/fernet.jsp.

Generating a Fernet Key for file encryption/decryption
To generate a Fernet key, run:
```p
from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key.decode())
```
- Copy the generated key and paste it when prompted in the compiler.
- After entering the key you will see that the script has been generated.

![img3](/images/3.png)

- Upon pressing enter, the script will be compiled into an executable.
- After a few seconds the executable will be compiled via PyInstaller and will be available in the `/dist` folder.

![img4](/images/5.png)

![img5](/images/6.png)


- You can now execute the compiled file on the system and get remote access on your desired Discord server.

## Testing the payload
- Upon executing `[filename].exe` you will receive a connection on the Discord Server from the bot. The bot will automatically create a new channel specifically used to operate the target machine where the file was executed.

![img6](/images/7.png)

- This enables the user to manage multiple devices efficiently at the same time using the C2 framework.
- You will receive a live screenshot of the target along with basic information of the target device.

![img7](/images/8.png)

- Next, you can use the help command with the desired prefix that you initially entered in the compiler to view the list of available commands.

![img8](/images/9.png)


- The possibilities are endless now. You can execute system commands using cmd `[command]` .  To change the working directory you will have to use `cd [path]` .
- You can also implant files on the target using `send`. Files from the target can be fetched and sent to the Discord server by the bot using `recv [file path]`.
- The help menu can be referred to understand the usage of other commands. For any more queries or problems you can create an Issue on the Github repository.
  
  
  ## Discord Commands
  
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
  | `send <path>` | Upload a file to the client in a specific location |
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
  - [ ] Webcam and microphone surveillance
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
  - [**Website**](https://avyukt-security.gitbook.io/home/team)
  
  
  ## Contact & Support
  
  For questions or issues, open a GitHub issue or submit a pull request.
  
  ---
  
  **Last Updated**: March 4, 2026  
  **Status**: Active Development  
  
