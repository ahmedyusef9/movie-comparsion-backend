FROM python:3.6

RUN mkdir /app
WORKDIR /app

RUN apt update && apt install vim --yes

RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app/
EXPOSE 5000
CMD ["python3" , "/app/main.py"]
