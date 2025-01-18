# FishyNotes 🐟 - Write-Up

## Challenge Description Recap
You were tasked with analyzing a suspicious Word document, uncovering its malicious components, and extracting the hidden flag.

---

## Solution

### 1. Inspecting the Document
The first step was to analyze the document using `oledump.py` to inspect its data streams:
```bash
oledump.py FishyNotes.doc
```
This revealed several streams, including one that contained a VBA macro.

---

### 2. Identifying the Macro Stream
Stream **8** was identified as containing VBA code. To view the macro, I extracted it with the following command:
```bash
oledump.py FishyNotes.doc -s 8 -v
```
This provided access to the VBA macro for further analysis.

---

### 3. Analyzing the VBA Code
In the macro code, I discovered a variable named `encodedPS`, which stored a Base64-encoded string. The macro also referenced a PowerShell command using the `-EncodedCommand` parameter. Here’s the relevant snippet:
```vba
Dim encodedPS As String
encodedPS = "RkxBR3tmaXNoeV9tYWNyb19kZXRlY3RlZH0="  
```

---

### 4. Decoding the Base64 String
I used a Base64 decoder to extract the hidden flag:
```bash
echo "RkxBR3tmaXNoeV9tYWNyb19kZXRlY3RlZH0=" | base64 -d
```
This revealed the flag:
```
FLAG{fishy_macro_detected}
```

---

## Flag
`FLAG{fishy_macro_detected}`

---

## Lessons Learned
This challenge demonstrated how to:
- Use `oledump.py` to inspect and extract streams from a Word document.
- Analyze VBA macros for encoded or hidden content.
- Decode Base64-encoded data to retrieve valuable information.

---

Good luck with your future DFIR adventures! 🚀
