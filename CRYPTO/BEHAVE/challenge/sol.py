## the input is 1
## the count is 1
## the output is 4b5255585146595f42515c6f515e515c494359436f0a6f575f5f546f5a5f524d

output_text = "4b5255585146595f42515c6f515e515c494359436f0a6f575f5f546f5a5f524d"

result_bytes = bytes.fromhex(output_text)


effective_key = ord("1") ^ 1 

recovered_bytes = bytes(b ^ effective_key for b in result_bytes)

flag = recovered_bytes[::]

print(flag.decode())
