FROM python:3.10-alpine

ENV MY_NODE_NAME=
ENV MY_POD_NAME=
ENV MY_POD_NAMESPACE=
ENV MY_POD_IP=

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

ENTRYPOINT ["python3"]
CMD ["app.py"]