FROM ubuntu:20.04 as chroot

RUN /usr/sbin/useradd --no-create-home -u 1000 user
RUN apt update -y
RUN apt install socat -y
RUN apt install python3 -y
RUN apt install python3-pip -y

RUN pip3 install pycryptodome

COPY source.py /home/user/source.py
COPY SECRET.py /home/user/SECRET.py
COPY run.sh /home/user/run.sh

WORKDIR /home/user

USER user

EXPOSE 5551

CMD socat TCP-LISTEN:5551,reuseaddr,fork EXEC:"/home/user/run.sh"
