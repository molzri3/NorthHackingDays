1-Open the final_challenge.pcap file in Wireshark.

2-Scan through the traffic to get an overview of the protocols and packets.

3-Apply the http filter 
![Capture d'écran 2025-01-16 224613](https://github.com/user-attachments/assets/3f313e2f-1873-44a6-8694-b8482c8c1955)
Here you can notice a file in the Get request named flag.txt 
Follow the HTTP stream to view the contents of flag.txt:

4-Right-click on the HTTP packet → Follow → HTTP Stream.
The contents of flag.txt will be displayed:
"Hey there, CTF player!

It seems like you've stumbled upon some interesting network traffic. 
Did you know that sometimes, data can travel through the most unexpected channels?

Good luck (: "
This hint suggests that the flag isn’t hiding in plain sight. It’s tucked away in an unexpected corner of the network traffic. But where?
the flag is hidden in a protocol that isn’t typically used for data transfer like http,ftp,ssh,smb....
So we need to look for packets that are often overlooked. ICMP is often ignored, so I’ll check that.

5-filter and dump only ICMP Echo request|reply packets

"tshark -r final_challenge.pcap -Y "icmp.type == 8" -T fields -e data.data | tr -d '\n'" or 
"tshark -r final_challenge.pcap -Y "icmp.type == 0" -T fields -e data.data | tr -d '\n'"
1. tshark
What it does: tshark is a command-line version of Wireshark. It’s used to analyze network traffic from PCAP files.

2. -r final_challenge.pcap
What it does: Specifies the input file (final_challenge.pcap) to read and analyze.

3. -Y "icmp.type == 8"
What it does: Applies a display filter to only show ICMP packets of type 8 (ICMP Echo Request, commonly used in ping).

4. -T fields -e data.data
What it does:

-T fields: Specifies that the output should be in field format.

-e data.data: Extracts the data.data field, which contains the payload of the ICMP packets.

5. | tr -d '\n'
What it does:

|: Pipes the output of the previous command to the next command.

tr -d '\n': Removes all newline characters (\n) from the output, making it a single continuous string.
The output of the command is:

"4b42445647365a524f413d3d3d3d3d3d504a5256365a33494d453d3d3d3d3d3d4d455a58534d4c424f513d3d3d3d3d3d4c3459574d583246474d3d3d3d3d3d3d47523458533343374f4d3d3d3d3d3d3d4e42515743334435"
This is a hexadecimal string that represents the combined payloads of all ICMP Echo Request packets.

Each pair of hexadecimal characters (e.g., 4b, 42, etc.) corresponds to a single byte of data.

6-Decoding the output : 
![image](https://github.com/user-attachments/assets/3813e710-8188-498a-b116-c61993ba7f4d)
after decoding from hex here is the output 
"KBDVG6ZROA======PJRV6Z3IME======MEZXSMLBOQ======L4YWMX2FGM======GR4XS3C7OM======NBQWC3D5"
if we try to identify its encoding using "dcode.fr" we are going to notice that's it's a Base 32 encoding 
so let's try to to decode it using cyberchef 
![image](https://github.com/user-attachments/assets/a0bdba21-9c3f-4f1e-abcc-f7252250f5f9)
"PGS{1pzc_ghaa3y1at_1f_E34yyl_shaal}"
easily we can notice that It's a rot cipher and exactly it's a ROT13 
so after decoding it we can easily get our flag 
![image](https://github.com/user-attachments/assets/308ee1ca-5f01-4b7e-95eb-0d7df7cb895d)

"CTF{1cmp_tunn3l1ng_1s_R34lly_funny}"
