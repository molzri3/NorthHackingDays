# Description 
Can find the path to the future ?

files to upload : server.c 

# File Descriptor Vulnerability Exploit

## Overview

This project demonstrates a file descriptor vulnerability where an attacker can read the content of any opened file using its file descriptor number.

## Vulnerability Explanation

File descriptors in Linux are numerical values assigned to opened files. Typically, they follow this pattern:

0: Standard Input (stdin)

1: Standard Output (stdout)

2: Standard Error (stderr)

3+: Additional file descriptors for opened files

The vulnerability allows reading file content by accessing /dev/fd/<fd_number>, where <fd_number> corresponds to an open file descriptor.

## Exploitation Steps

Identify an active file descriptor (FD) associated with a sensitive file.

Use cat or less to view the file’s content through /dev/fd/<fd_number> >> /dev/fd/6 for my case .
