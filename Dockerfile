FROM python:3
ADD requests_flask.py /
ADD requirements.txt /
RUN pip install -r requirements.txt
CMD [ "python", "./requests_flask.py" ]
