FROM python:3.6
MAINTAINER XenonStack

RUN mkdir -p /booksfrontend/src

WORKDIR /booksfrontend/src

COPY requirements.txt /booksfrontend/src
RUN pip install --no-cache-dir -r requirements.txt

COPY . /booksfrontend/src

ENV APP_ENV development
ENV apiURL=http://192.168.99.100:30103

EXPOSE 5040

CMD ["python3", "main.py"]
