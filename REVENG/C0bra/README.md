# Challenge: C0bra

## Description
People say cobra is long; let's see how long it really is.

## Flag
`NHD{C0br4_3nDK}`

## Solution
To solve this challenge, follow these steps:

1. **Obtain the Binary**: Download the provided binary file associated with the challenge.
2. **Decompile the Binary**: Use the `uncompyle6` tool to decompile the binary. This tool helps in converting Python bytecode back into the equivalent Python source code.
   ```sh
   uncompyle6 -o . <path_to_binary>
   ```