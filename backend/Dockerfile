# base image
FROM python:3.9

# copy just the requirements.txt first to leverage Docker cache
# install all dependencies for Python app
WORKDIR /app

COPY requirements.txt .

# install dependencies in requirements.txt
RUN pip install -r requirements.txt

# copy all content to work directory /app
COPY . .

# specify the port number the container should expose
EXPOSE 8000

# run the application
CMD ["python", "manage.py", "runserver"]