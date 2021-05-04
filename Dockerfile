FROM ubuntu:latest

RUN apt-get update -y && apt-get install -y python3-pip python3-dev
COPY . /home/server/
WORKDIR /home/server/
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3" ]
CMD [ "Server.py" ]

# docker build -t now-weather .
# docker run --neame now-weather -p 5000:5000 now-weather