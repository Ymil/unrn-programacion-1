FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN mv /bin/rm /bin/rm.real && \
    printf '#!/bin/sh\necho "El comando rm está deshabilitado en este entorno de práctica."\n' > /bin/rm && \
    chmod +x /bin/rm

RUN apt-get update && \
    apt-get install -y \
        openssh-server \
        nano \
        vim \
        python3 \
        python3-pip \
        python3-venv \
        bash \
    && mkdir /var/run/sshd \
    && apt-get clean

RUN useradd -m -s /bin/bash alumno && \
    echo "alumno:alumno" | chpasswd
    
EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]