# Use a lightweight base image
FROM ubuntu:20.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    netcat \
    && rm -rf /var/lib/apt/lists/*

# Copy the challenge code and flag.txt
COPY challenge.c /app/challenge.c
COPY flag.txt /app/flag.txt

# Compile the challenge
WORKDIR /app
RUN gcc -fno-stack-protector -z execstack -o challenge challenge.c

# Expose the port
EXPOSE 12345

# Run the challenge
CMD ["./challenge"]
