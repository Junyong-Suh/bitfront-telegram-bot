FROM frolvlad/alpine-python3
ADD *.py /
ADD requirements.txt /
RUN pip3 install -r requirements.txt
CMD [ "python", "./main.py" ]
