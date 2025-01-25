# DIR NIYA 💻 - Write-Up

## Challenge Description Recap
You were tasked with analyzing a suspicious PowerShell activity captured in Windows Event Logs, uncovering the malicious command, and extracting the hidden flag.

---

## Solution

### 1. Investigating the Logs
The first step was to open the provided **PowerShell Event Log file (`dir_niya.evtx`)** in a log analysis tool such as Event Viewer or a third-party tool like Log Parser Studio.

### 2. Locating Suspicious PowerShell Commands
By filtering the log entries for **Event ID 4104** (PowerShell script block logging), I found a suspicious encoded command executed by the attacker:
```plaintext
powershell.exe -enc JABkAGkAcgBfAG4AaQB5AGEAIAA9ACAAJwBHADUAVQBYAEkASQBEAEUATwBKADIARwBTAEkARABPAE4ARgA0AFcAQwBJAEQAVQBPAE4AMgBHAEMAMgBEAE0ARQBCAFUARwBDAFoAQgBBAE0AWgBXAEcAQwBaAFoAQQBJAE4ASwBFAE0ANgAzAFgATgBCAFgAVgA2ADIARABCAE8ATgBQAFgASQA0AFQAVgBPAE4AMgBGADYAMgBMAFQATwBOADIAVwBLADQAMgA3AE8ANQBVAFcAWQAzAEMANwBOAFoAUwBYAE0AWgBMAFMATAA1AFQAVwBLADUAQwA3AE4AVgBTAFgAMgA9AD0APQAnAA
```

### 3. Decoding the Base64 Command
The encoded command was Base64-encoded. I decoded it using cyberchef:
This revealed the following PowerShell command:
```powershell
$dir_niya = 'G5UXIIDEOJ2GSIDONF4WCIDUON2GC2DMEBUGCZBAMZWGCZZAINKEM63XNBXV62DBONPXI4TVON2F62LTON2WK427O5UWY3C7NZSXMZLSL5TWK5C7NVSX2==='
```

### 4. Decoding the Base32 String
The decoded command assigned a Base32-encoded string to the variable `$dir_niya`. I used a Base32 decoder to decode it:
```bash
echo "G5UXIIDEOJ2GSIDONF4WCIDUON2GC2DMEBUGCZBAMZWGCZZAINKEM63XNBXV62DBONPXI4TVON2F62LTON2WK427O5UWY3C7NZSXMZLSL5TWK5C7NVSX2===" | base32 -d
```
This revealed the flag:
```
7it drti niya tstahl had flag CTF{who_has_trust_issues_will_never_get_me}
```

---

## Flag
`CTF{who_has_trust_issues_will_never_get_me}`

---

## Lessons Learned
This challenge highlighted the importance of:
- Recognizing and investigating encoded PowerShell commands in event logs.
- Leveraging built-in tools like Event Viewer and PowerShell for forensic analysis.
- Decoding multiple layers of obfuscation (e.g., Base64 and Base32) to uncover hidden content.

Great work, investigator! 💪
