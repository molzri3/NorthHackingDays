# Fireside Secrets - Write-Up
## **Overview**
---

The challenge involves multiple layers of skills and techniques:

1-Decrypting Firefox passwords stored in a user profile.
2-Finding a hidden directory containing a password-protected flag.zip file.
3-Extracting the flag using the decrypted password.

---

## **Exploring the VHDX File**
first we need to unzip the **Profiles.zip** which contains the vhdx file.
but you can see that a password is required 

![image](https://github.com/user-attachments/assets/22dc09b4-b736-4ec4-9e7a-bbac0056a256)

To proceed, we need to crack the ZIP file password using **fcrackzip** or **john**.
```bash

fcrackzip -v -u -D -p /usr/share/wordlists/rockyou.txt profiles.zip
found file 'firefox_profiles.vhdx', (size cp/uc 60867448/239075328, flags 9, chk 4c42)


PASSWORD FOUND!!!!: pw == operationcwal


```

