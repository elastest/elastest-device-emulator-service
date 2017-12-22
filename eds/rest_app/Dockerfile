FROM python:2-alpine

# Set Image Labels
ARG GIT_COMMIT=unspecified
LABEL git_commit=$GIT_COMMIT

ARG COMMIT_DATE=unspecified
LABEL commit_date=$COMMIT_DATE

ARG VERSION=unspecified
LABEL version=$VERSION 

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip install -r requirements.txt
COPY . /usr/src/app

ENV EDS_PORT 8080
ENV EDS_CHECK_PORT 9090

EXPOSE 8080
EXPOSE 9090

ENTRYPOINT ["python"]

CMD ["resty.py"]