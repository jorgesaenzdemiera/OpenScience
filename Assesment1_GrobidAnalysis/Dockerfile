FROM python:3.11-buster

WORKDIR /home

COPY requirements.txt .
COPY code /code
COPY input /input
COPY output /output


RUN pip install -r requirements.txt

RUN git clone https://github.com/kermitt2/grobid_client_python && cd grobid_client_python && python setup.py install
RUN cd ../code

CMD ["python3", "grobid.py"]