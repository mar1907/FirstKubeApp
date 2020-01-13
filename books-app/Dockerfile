FROM python:3.6
MAINTAINER XenonStack

RUN mkdir -p /books/src

WORKDIR /books/src

COPY requirements.txt /books/src
RUN pip install --no-cache-dir -r requirements.txt

COPY . /books/src/app

ENV APP_ENV development

EXPOSE 5035

CMD ["python3", "app/books.py"]
