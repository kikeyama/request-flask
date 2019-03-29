FROM python:3
ADD requests_flask.py /
ADD requirements.txt /
ENV HTTP_HOST <HTTP_HOST>
ENV HTTP_PORT <HTTP_PORT>
RUN pip install -r requirements.txt
CMD [ "python", "./requests_flask.py" ]
