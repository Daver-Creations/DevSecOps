FROM python:3.11.8-alpine3.19

WORKDIR /app

COPY *.txt .

RUN pip3 install -r requirements.txt

COPY . .

RUN rm -f requirements.txt

EXPOSE 80

CMD ["python3", "main.py"]