# Use an Ubuntu base image and enable 32-bit architecture support
FROM ubuntu:18.04

# Install 32-bit libraries and socat
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y libc6-i386 socat && \
    rm -rf /var/lib/apt/lists/*

# Create a working directory
WORKDIR /challenge

# Copy the challenge binary and flag file into the image
COPY vuln /challenge/vuln
COPY flag.txt /challenge/flag.txt

# Set proper permissions (vuln should be executable, flag.txt readable)
RUN chmod 755 vuln && chmod 644 flag.txt

# Create a non-root user for running the challenge
RUN useradd -m ctf && chown -R ctf:ctf /challenge
USER ctf

# Expose the challenge port
EXPOSE 9999

# Start socat to listen on port 9999 and spawn the vuln binary for each connection
CMD ["socat", "TCP-LISTEN:9999,reuseaddr,fork", "EXEC:./vuln,pty,stderr"]
