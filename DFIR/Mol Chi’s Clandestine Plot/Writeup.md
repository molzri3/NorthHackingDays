# Mol Chi’s Clandestine Plot - Write-Up
---

## **Overview**
The challenge involves multiple layers of skills and techniques:
1. Extracting data from a USB directory structure.
2. Decoding hidden credentials.
3. Performing steganography on an image file to retrieve the first part of the flag.
4. Reversing an executable file to uncover a PowerShell script.
5. Finding and analyzing a GitHub repository for the second part of the flag.

---

## **Step 1: Exploring the USB Structure**
Analyze the given USB using FTK imager 
![image](https://github.com/user-attachments/assets/ce4939d9-aa20-402e-904f-4e96ad28fd14)
So here is the structure of the usb drive 
```bash
.
├── Confidential
│   ├── creds.txt
│   └── reminder.txt
├── music
│   └── yaManMalakni.mp3
├── Pictures
│   └── secret_meeting.jpg
└── Programs
    └── installer.exe
```
### **Initial Observations:**
- **`Confidential` folder**: Contains suspicious text files like `creds.txt`.
- **`Pictures` folder**: Holds `secret_meeting.jpg`, which might involve steganography.
- **`.Programs` folder**: Contains `installer.exe`, which requires reverse engineering.

---

## **Step 2: Decoding Credentials**
But before trying to decode the Credentials given let's read the reminder.txt file 
```bash
Subject: Important Meeting - Don't Forget!

From: si l'admin mol chi admin@molchi.ma
To: l3abd l3abd@bladi.dz

Message:

Hey l3abd,

Listen carefully, or rather, read this and engrave it in your mind. The meeting is on Tuesday, February 25th. Donâ€™t forget, or youâ€™ll see what's coming your way. I donâ€™t want any excuses, no "I forgot" or "I had something else to do." Youâ€™ve been warned.

Be there, on time, and prepare everything we need also don't forget to bring with you the secret things that I gived you, you gonna need it !!!. I'm counting on you, but more importantly, Iâ€™m watching you.

Sincerely (if you can call it that),
Si l'admin


```
This email conveys a strong sense of urgency and authority from "si l'admin mol chi" to "l3abd."
it indicates That there is a meeting in Tuesday, February 25th and There is a mention of "the secret things I gave you" suggests "l3abd" has possession of critical or confidential materials crucial to the meeting.
which hints us that we need to use the creds provided in something related to the meeting.
#### Let's take a look to the provided creds in creds.txt file

```bash
Si l'admin Mol chi :MDEwMTAwMTEgMDExMDAxMDEgMDExMDAwMTEgMDExMTAxMDEgMDExMTAwMTAgMDExMDAxMDEgMDEwMTAwMDAgMDExMDAwMDEgMDExMTAwMTEgMDExMTAwMTEgMDExMTAxMTEgMDExMDExMTEgMDExMTAwMTAgMDExMDAxMDAgMDAxMTAwMDEgMDAxMTAwMTAgMDAxMTAwMTEgMDAxMDAwMDE=

```
we can notice that This is a **Base64-encoded string** , let's try to decode it using cyberchef
![image](https://github.com/user-attachments/assets/27fc867c-c3fa-440f-9de2-5ee7e79c1100)
as you see it still encoded in binary so now convert the binary code to ASCII text 
![image](https://github.com/user-attachments/assets/e2bc0638-1f59-4107-bbf5-325689d61565)
and here we go this is the decoded password : **SecurePassword123!**

---

## **Step 3: Extracting the First Part of the Flag**
![secret_meeting](https://github.com/user-attachments/assets/358bbd67-cb40-449e-bee3-2f54ad709784)

Use the **passphrase** to extract hidden data from **secret_meeting.jpg** with **steghide**:
```bash
steghide extract -sf secret_meeting.jpg                            
Enter passphrase:
wrote extracted data to "flag_part1.txt".

cat flag_part1.txt 
CTF{Usb_r3v3Rs3

```
#### Here we go the first part of the flag : CTF{Usb_r3v3Rs3

---

## **Step 4: Reversing the Executable**

the first thing to do is to use the **strings** command to search for readable text
```bash
strings installer.exe | head         
!This program cannot be run in DOS mode.
UPX0
UPX1
UPX2
4.22
UPX!
F>j|V#
9e>c
-r A
sXF J
```
The presence of **UPX0**, **UPX1**, and **UPX2** strongly indicates that the executable is packed with **UPX**.
Packing is typically used to:
**Reduce file size**: UPX compresses executables to save storage space and reduce transfer times.
**Obfuscate code**: While not designed for this purpose, packing can hinder reverse engineering because the packed sections need to be unpacked to access the actual code.
we can verify easily that our file is packed with upx 
```bash
upx -t installer.exe

                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2024
UPX 4.2.4       Markus Oberhumer, Laszlo Molnar & John Reiser    May 9th 2024

testing installer_obfus.exe [OK]

Tested 1 file.

```
Then we unpack it 
```bash
upx -d installer.exe                 
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2024
UPX 4.2.4       Markus Oberhumer, Laszlo Molnar & John Reiser    May 9th 2024

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
    116537 <-     63289   54.31%    win64/pe     installer_obfus.exe

Unpacked 1 file.
```
