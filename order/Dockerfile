FROM ubuntu:latest

# set a directory for the app
WORKDIR /app

# copy all the files from the host folder to the container
COPY . .

# update apt-get repository 
RUN apt-get update -y	


# install python3
RUN apt-get install python3 -y

# install pip3
RUN apt-get install python3-pip -y

# Run client.py when the container launches
CMD ["python", "order.py"]