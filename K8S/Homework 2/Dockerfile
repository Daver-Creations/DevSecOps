# Create a new build stage from a base image
FROM python:3.12.2-slim-bookworm

# Change working directory
WORKDIR /app

# python needs a requirements file to install the dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy files and directories
COPY . .

# setting flask app env variable
ENV FLASK_APP=computers_api.py

EXPOSE 5000

# instructs instructs Docker to run our Flask app as a module
# instructs Docker to make the container available externally
# and pass the host port
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
