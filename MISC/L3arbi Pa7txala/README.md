# Description :
the flag is in the following path : /dev/flag.txt
if you can deal with pa7txala you can get the flag :)

files to upload : server.c

# Symbolic Naming Bypass Exploit

## Overview

This exploit leverages symbolic naming instead of using traditional paths like /dev to access restricted files.

## How It Works

Instead of accessing /dev/* directly, some systems support alternative symbolic paths, such as ~sys/, which can be used to reference system resources. This allows bypassing certain security mechanisms that only check for standard paths.

## Exploit Command

```cat ~sys/flag.txt```

This command retrieves the contents of flag.txt using symbolic naming instead of direct /dev access.
