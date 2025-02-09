# Challenge Writeup

## Challenge Description
Espada is a group of villains created by Molzri3. They fear nothing—except the absolute path.

## Vulnerability Analysis
The application tries to prevent directory traversal by removing occurrences of `../` and `..\` using `replace` functions or regex. However, attackers can bypass these protections using nested traversal sequences or encoded payloads.

### Key Code Issues:
1. **Improper Sanitization:**
   - The function `sanitizePath(input)` replaces `../` and `..\`, but does not account for alternative encodings or deeply nested traversal sequences.
   
2. **Vulnerable File Resolution:**
   - The `resolvePath(input)` function still allows absolute paths to be resolved outside the intended directory if an attacker constructs the right payload.

## Exploitation
An attacker can exploit this vulnerability to read arbitrary files on the server, such as `flag.txt`, by sending a specially crafted payload.

### Exploit Payload:
```
http://server-ip:3333/view?file=....//....//....//flag.txt
```
## Flag
```
NHD{6leach_is_0verrated_for_sure}
```
