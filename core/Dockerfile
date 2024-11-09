FROM python:3.12.3

WORKDIR /app

COPY . /app

# INSTALL DEPENDENCIES
RUN pip install -r requirements.txt

#EXPOSE 5000

# RUN THE SERVER
CMD python -m server.start
