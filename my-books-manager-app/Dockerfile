FROM python:3.6
MAINTAINER XenonStack

RUN mkdir -p /booksfrontend/src

WORKDIR /booksfrontend/src

COPY requirements.txt /booksfrontend/src
RUN pip install --no-cache-dir -r requirements.txt

COPY . /booksfrontend/src

ENV APP_ENV development
ENV apiURL=IP:PORT

EXPOSE 5040

CMD ["python3", "main.py"]
