FROM ubuntu:20.04

RUN apt-get update && apt-get install -y socat gcc

RUN useradd -m ctf

WORKDIR /home/ctf

COPY vuln.c .
RUN gcc -no-pie -fno-stack-protector -z execstack -o vuln vuln.c --static
COPY flag.txt /flag.txt


RUN chmod 755 ./vuln
RUN chmod 644 /flag.txt


USER ctf
EXPOSE 1337

CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:./vuln
