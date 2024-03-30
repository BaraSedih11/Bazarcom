FROM python:latest

# set a directory for the app
WORKDIR /app

# COPY requirements.txt .
# RUN pip install -r requirements.txt

# copy all the files from the host folder to the container
COPY . .

# update apt-get repository 
# RUN apt-get clean && apt-get update -y


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# RUN apt-get install python3-pip -y
# RUN pip install Flask
# RUN pip install flask_sqlalchemy
# RUN pip install flask_marshmallow
# RUN pip install marshmallow


EXPOSE 5050

# Run client.py when the container launches
CMD ["python3", "gateway.py"]