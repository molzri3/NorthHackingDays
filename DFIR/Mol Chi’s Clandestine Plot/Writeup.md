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


