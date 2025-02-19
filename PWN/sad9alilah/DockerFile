FROM ubuntu:20.04

RUN apt-get update && apt-get install -y socat gcc

RUN useradd -m ctf

WORKDIR /home/ctf

COPY vuln ./vuln
COPY flag.txt ./flag.txt
Copy canary.txt ./canary.txt


RUN chmod 755 ./vuln
RUN chmod 644 /flag.txt


USER ctf
EXPOSE 7777

CMD socat TCP-LISTEN:7777,reuseaddr,fork EXEC:./vuln
