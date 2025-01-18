# Use a lightweight base image
FROM ubuntu:20.04
# Copy the challenge binary and flag
COPY jortomat_al_ma3ida /app/challenge
COPY flag.txt /app/flag.txt
# Set permissions
RUN chmod 755 /app/challenge
RUN chmod 644 /app/flag.txt
# Expose the port (informational)
EXPOSE 12345
WORKDIR /app
# Run the challenge
CMD ["/app/challenge"]
