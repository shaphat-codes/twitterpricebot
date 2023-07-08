
FROM python:3.10-slim
EXPOSE 8000

RUN apt-get update \
 && apt-get install wget unzip zip -y

#for logging

ENV PYTHONUNBUFFERED 1



#for not creating .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

#specifying our working directory
WORKDIR /app/pricebot

#copying requirements.txt file to the working directory


COPY requirements.txt /app/pricebot/
RUN apt-get update
# Install Chrome WebDriver
RUN apt-get install -y wget
RUN apt-get update && apt-get install -y gnupg
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \ 
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get -y install google-chrome-stable



RUN pip install -r requirements.txt
# Build psycopg2-binary from source -- add required dependencies

#copying the content of the backend application into our Docker container.
COPY . /app/pricebot/




