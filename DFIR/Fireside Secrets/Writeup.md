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

### Now let's unzip the file using the password found 

```bash

unzip profiles.zip
Archive:  profiles.zip
[profiles.zip] firefox_profiles.vhdx password: 
  inflating: firefox_profiles.vhdx  


```
### Now we need to mount the disk to our machine 

```bash

sudo modprobe nbd
sudo qemu-nbd --connect=/dev/nbd0 firefox_profiles.vhdx
mkdir /mnt/vhdx
lsblk                      
NAME     MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda        8:0    0 80.1G  0 disk 
└─sda1     8:1    0 80.1G  0 part /
sr0       11:0    1 1024M  0 rom  
nbd0      43:0    0  200M  0 disk 
├─nbd0p1  43:1    0   16M  0 part 
└─nbd0p2  43:2    0  182M  0 part 
nbd1      43:32   0    0B  0 disk 
nbd2      43:64   0    0B  0 disk 
nbd3      43:96   0    0B  0 disk 
nbd4      43:128  0    0B  0 disk 
nbd5      43:160  0    0B  0 disk 
nbd6      43:192  0    0B  0 disk 
nbd7      43:224  0    0B  0 disk 
nbd8      43:256  0    0B  0 disk 
nbd9      43:288  0    0B  0 disk 
nbd10     43:320  0    0B  0 disk 
nbd11     43:352  0    0B  0 disk 
nbd12     43:384  0    0B  0 disk 
nbd13     43:416  0    0B  0 disk 
nbd14     43:448  0    0B  0 disk 
nbd15     43:480  0    0B  0 disk
sudo mount /dev/nbd0p2 /mnt/vhdx


```
