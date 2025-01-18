# FishyNotes 🐟 - Write-Up

## Challenge Description Recap
You were tasked with analyzing a suspicious Word document, uncovering its malicious components, and extracting the hidden flag.

---

## Solution

### 1. Inspecting the Document
The first step was to analyze the document using `oledump.py` to inspect its data streams:
```bash
oledump.py FishyNotes.docm
```
This revealed several streams, including **Stream A3**, which contained a VBA macro.

---

### 2. Identifying the Macro Stream
To view the contents of **Stream A3**, I extracted it using the following command:
```bash
oledump.py FishyNotes.docm -s A3 -v
```
This provided access to the VBA macro for further analysis.

---

### 3. Analyzing the VBA Code
In the macro code, I noticed several key points:
- The flag was stored in two parts as `part1` and `part2`, making it slightly obfuscated:
  ```vba
  part1 = "Q1RGe2Zpc2h5X21hY"
  part2 = "3JvX2RldGVjdGVkfQ=="
  encodedPS = part1 & part2
  ```
  When combined, this forms the Base64-encoded string:  
  `Q1RGe2Zpc2h5X21hY3JvX2RldGVjdGVkfQ==`

- The macro also created an obfuscated PowerShell command using the encoded string:
  ```vba
  cmdStart = "powershell.exe "
  cmdEnd = "-EncodedCommand " & encodedPS
  Command = cmdStart & cmdEnd
  ```

### 4. Decoding the Base64 String
The `encodedPS` variable contained the Base64-encoded flag, which I decoded using a Base64 decoder:
```bash
echo "Q1RGe2Zpc2h5X21hY3JvX2RldGVjdGVkfQ==" | base64 -d
```
This revealed the flag:
```
CTF{fishy_macro_detected}
```

---

## Flag
`CTF{fishy_macro_detected}`

---

## Lessons Learned
This challenge demonstrated how:
- VBA macros can be slightly obfuscated to make analysis more challenging.
- Encoded data is often stored in parts to avoid detection by simple string extraction tools.
- Tools like `oledump.py` are essential for inspecting and extracting suspicious streams in documents.

Good luck with future DFIR challenges! 🚀
