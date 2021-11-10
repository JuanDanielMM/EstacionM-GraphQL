FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /EMeteorologica
WORKDIR /EMeteorologica
COPY requirements.txt /EMeteorologica/
RUN pip install -r requirements.txt
COPY . /EMeteorologica/
