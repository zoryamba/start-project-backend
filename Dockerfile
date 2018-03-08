FROM python:3.6.4
WORKDIR /backend/src
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt
