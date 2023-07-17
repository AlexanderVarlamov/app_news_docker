FROM python:3.9.17-slim-bullseye

ADD ./client /client
WORKDIR /client
RUN python -m venv venv
RUN . ./venv/bin/activate
RUN pip install -r requirements.txt

EXPOSE 5111


CMD ["python", "main.py"]