import re
import scapy.all
import requests
import bz2
import sys
import os
import platform

# Key words to filter overwatch demo packages from uninteresting ones - Thanks for constructing the regex: https://github.com/takeshixx/csgo-overwatcher
DEMO_FILENAME = re.compile(r'GET /730/(\d+_\d+.dem.bz2)')
URL_PATH = re.compile(r'GET (/730/\d+_\d+.dem.bz2)')
FILE_HOST = re.compile(r'Host: (replay\d+.valve.net)')
FILE_HOST2 = re.compile(r'Host: (replay\d+.wmsj.cn)') # two different hosts can occur

version = "1.1"

# Check for root privileges on Linux
if platform.system() == "Linux":
    if os.getuid() != 0:
        print("\nPlease run this script with root privileges!\nI'm otherwise not able to sniff on your network for packages that contain the demo file.")
        exit()

# Display welcome text
print(f"\nCSGO-Overwatch-Downloader v{version} by 3urobeat")
print("---------------------------\n")

# Check if scapy is able to sniff -> otherwise user is probably using Win10 and is missing win10pcap
try:
    scapy.all.sniff(count=1, iface=None, store=False)
except RuntimeError:
    print("\nError!\n----\nIt seems like you are on Windows and haven't installed Win10Pcap.\nPlease download it from here: http://www.win10pcap.org/download/")
    exit()
    

# Defining all functions to call them one after another
def finish(filename):   
    # Print console command and exit
    if len(sys.argv) > 1:
        print("\n----\nPut this command into your csgo console to play the demo:")
    else:
        print("\n----\nAfter moving the demo file to " + r'Counter-Strike Global Offensive\csgo\\' + " type this into the console:")
        
    print("playdemo " + filename.replace(".dem", "").replace(".bz2", ""))
    print("----\n")
    
    print("Finished!")
    exit()

def downloaddemo(demourl, filename):
    print("Downloading Overwatch demo...")
    file = requests.get(demourl) # Download file with requests
    
    print("Decompressing file...")
    decompressed_file = bz2.decompress(file.content) # demo files ship as bz2 files -> decompress before saving
    
    # idea: check default installation paths? Maybe get the csgo installation path from registry? or just leave it like this
    if len(sys.argv) > 1: # Check if user provided a folder to the csgo installation
        print(f"Saving file to {str(sys.argv[1])}...")
        
        if platform.system() == "Windows":
            slash = "\\" # Windows is weird and uses backslashes
        else:
            slash = "/"
        
        open(str(sys.argv[1]) + slash + str(filename).replace(".bz2", ""), 'wb').write(decompressed_file) # Save file with filename we acquired from packet info but remove bz2 because we just decompressed it
    else:
        print("\nSaving file to the script's directory because you haven't provided a path to your CS:GO installation.\nYou will have to move the demo to the " + r'Counter-Strike Global Offensive\csgo\\' + " yourself in order to watch it.")
        open(str(filename).replace(".bz2", ""), 'wb').write(decompressed_file)
    
    finish(str(filename))

def checkpacket(pkt):
    # Got some inspiration on how to analyse the packet from here (Thanks again ^^): https://github.com/takeshixx/csgo-overwatcher
    
    packet = str(pkt) # Convert packet information to string

    url_matches = URL_PATH.findall(packet) # get all matches with URL_PATH in an array
    host_matches = FILE_HOST.findall(packet)
    host2_matches = FILE_HOST2.findall(packet)
       
    if url_matches and any([host_matches, host2_matches]): # check if packet info has url matches and if one of the both possible hosts match
        if host_matches: # Check which one of the two hosts is the matching one
            demourl = f'http://{host_matches[0]}{url_matches[0]}' # Build URL from both matches
        else:
            demourl = f'http://{host2_matches[0]}{url_matches[0]}'
            
        print(f"Found a demo! ({demourl})")
        filename = DEMO_FILENAME.findall(packet)[0]
        
        downloaddemo(demourl, filename) # start downloading the demo we found

def sniffnetwork():
    # Scan network with scapy
    print("Please click on Download in CS:GO now.")
    print('Sniffing on your network for Overwatch downloads...')
    scapy.all.sniff(filter='tcp port 80',prn=checkpacket) # pass sniffed packet to checkpacket
    
sniffnetwork() # Start sniffing
