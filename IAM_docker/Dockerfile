# https://www.builtydata.com/
# author: Harut Grigoryan

# The definition of the docker image
# to run the Builty scraping framework 

FROM --platform=linux/amd64 amazonlinux:latest
# FROM --platform=linux/amd64 amazonlinux:2023.3.20240108.0

ENV PATH=$PATH:/root/.local/bin/
ENV PYTHONPATH=$PYTHONPATH:/usr/src/

RUN yum -y update && yum -y install \
  gcc glibc-devel make which \
  python3 python3-devel postgresql-devel

RUN curl -O https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py --user

COPY requirements.txt /
COPY db_access.py /
COPY entrypoint.sh /
RUN pip3 install --no-cache-dir -r /requirements.txt

# install Node JS
RUN yum install -y nodejs

# install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" 
RUN unzip awscliv2.zip -d /usr/src/ 
RUN /usr/src/aws/install

# install SSM plugin
RUN yum install -y https://s3.amazonaws.com/session-manager-downloads/plugin/latest/linux_64bit/session-manager-plugin.rpm

# install Telnet
RUN yum -y install telnet

# Run bach in the container
# docker run --rm -it --entrypoint bash <image-name-or-id>

# Enter a running container
# docker exec -it <container-name-or-id> bash

RUN chmod +x entrypoint.sh
CMD ["./entrypoint.sh"]
# CMD [ "/bin/bash", "-c", "echo 'Hello World'; sleep infinity"]
# CMD [ "python3", "db_access.py"]