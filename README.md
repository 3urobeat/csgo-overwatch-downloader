# csgo-overwatch-downloader
This python script allows you to easily download the uncensored version of your Overwatch Case!  

![Screenshot](https://raw.githubusercontent.com/HerrEurobeat/csgo-overwatch-downloader/master/.github/img/demo.png)

## Download
Make sure to have [Python 3](https://www.python.org/downloads/) (`Windows x86-64 executeable installer`) installed.  
If you are using Linux then you should be able to download python3 from your distribution's packet manager or you probably already have it installed.  

If you don't know if you have Python installed, open a `cmd` and type `py --version` or `python --version`.  
If the command is not recognized you will have to install it from the link above.  
> I haven't tested the Microsoft Store version of Python 3.  

Make sure to have `Win10Pcap` or `Ncap` installed if you are running on Windows.  
If you are not sure if you have it installed just proceed - the script will tell you.  

[Download this script](https://github.com/HerrEurobeat/csgo-overwatch-downloader/archive/master.zip) and extract the folder.  

Open the folder in a `cmd`, `PowerShell` or any other terminal.  
You can do this on Windows by clicking on "File" in the top left corner of your file explorer and then clicking on `Open PowerShell` or `Open Command Prompt`.  
  
**Windows:**  
Type `py -m pip install scapy requests` and let the two packages install.  
If `py` doesn't work for you try `python` or `python3`. I'm not sure which one works now since Microsoft added Python into their stupid Store.  
  
**Linux:**  
Make sure to install the packages using root privileges. Type `sudo pip3 install scapy requests`, enter your root password and let the two packages install.  

## Usage
Start the script by typing `py downloader.py "csgo_path"` into your terminal and replace `csgo_path` with the path to your csgo folder.  
If you are on Linux, make sure to start the script as root! Example: `sudo python3 downloader.py "csgo_path"`  

If you are using the default location on Windows it is probably `C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo`.  
If you changed your installation path you will probably know where you installed CS:GO. If not, right click on CS:GO in your Steam library, open the Properties, click on `Local Files` and then on `Browse`. This will open the folder in your file explorer.  
  
> Make sure your path is in quotation marks and has no slash at the end!  
> Example Windows: `py downloader.py "C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo"`
> Example Linux: `sudo python3 downloader.py "/media/tomg/SSD/Steam Games/steamapps/common/Counter-Strike Global Offensive/csgo"`  

If you don't provide a path you will have to move the demo to your folder by yourself in order to be able to play it from the csgo console.  

The script will now wait for you to click on the `Download` button in your CS:GO Overwatch page.  
> If you already downloaded an Overwatch case, go into your `Counter Strike Global Offensive\csgo` folder and delete the `myassignedcase.evidence` file and restart CS:GO.  

The script will now download your uncensored Overwatch Case!  
Have fun!  

Thanks to [takeshixx](https://github.com/takeshixx/csgo-overwatcher) for helping me to filter CS:GO overwatch packets by having his source code available on GitHub!  

## FAQ
Q: Will this get me banned?  
A: No. This script doesn't interfere with your game - it just sniffs on the network traffic when downloading the overwatch case and gets the URL from where CS:GO downloads the evidence. It's the same method like using Wireshark - just automated with Python.  
