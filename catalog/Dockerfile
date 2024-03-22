FROM python:latest

# set a directory for the app
WORKDIR /app

# COPY requirements.txt .
# RUN pip install -r requirements.txt

# copy all the files from the host folder to the container
COPY . .

# update apt-get repository 
# RUN apt-get clean && apt-get update -y


# install python3
# RUN apt-get install python3 -y

# install pip3
# RUN apt-get install python3-pip -y
RUN pip install Flask
RUN pip install flask_sqlalchemy
RUN pip install flask_marshmallow
RUN pip install marshmallow


EXPOSE 5000

# Run client.py when the container launches
CMD ["python3", "./catalog.py"]