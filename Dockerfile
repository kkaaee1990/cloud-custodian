FROM ubuntu:latest

WORKDIR /home/custodian/aws

RUN apt update
RUN apt -y install python3
RUN apt -y install pip
RUN apt -y install curl
RUN apt -y install zip
RUN pip install c7n
RUN pip install c7n-mailer
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install
RUN /usr/local/bin/aws --version
RUN ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update
RUN rm -rf aws
RUN rm awscliv2.zip
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

COPY python.py python.py

EXPOSE 80

CMD ["tail","-f","/bin/bash"]



 