FROM python:2-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

ENV ESM_PORT 8080
ENV ESM_CHECK_PORT 9090

EXPOSE 8080
EXPOSE 9090

ENTRYPOINT ["python"]

CMD ["resty.py"]