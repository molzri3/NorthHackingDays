# **Walkthrough: Tadribat**

### **Step 1: Understanding the Challenge**

You are given 16 PNG images, but they cannot be opened due to corrupted metadata. Even if you attempt to recover or fix the metadata, the images remain empty, providing no visible clues.

### **Step 2: Changing the Approach**

Since the metadata corruption appears intentional, a different approach is needed. By extracting and analyzing the modified hexadecimal values within the metadata of each image, you notice a pattern: the values are not random.

### **Step 3: Collecting the Hex Data**

Since the images are already in a specific order, you collect the modified hex values sequentially from each image and combine them into a single dataset.

### **Step 4: Using CyberChef for Analysis**

Once the hex values are collected, you input them into CyberChef, a powerful tool for data analysis and cryptography tasks. You use the **"From Hex"** operation to convert the hex string into raw data.

### **Step 5: Detecting XOR Encryption**

After conversion, the output appears to be encoded. A common encoding method used in CTF challenges is **XOR encryption**. Using the **"XOR Brute Force"** operation in CyberChef with a key length of 1, you attempt decryption.

### **Step 6: Recovering the Flag**

Upon running the XOR brute-force attack, one of the key candidates successfully decrypts the hidden message, revealing the flag:

🟢 **Flag: `CTF{h3x_X0r_fun}`**

🟢 Description : 16 corrupted PNG images hide a secret—Can you uncover what’s truly hidden.
