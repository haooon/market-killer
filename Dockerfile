FROM python:3.6
ENV PATH /usr/local/bin:$PATH
ADD ./pipinstall /code/pipinstall
WORKDIR /code
RUN pip install -r pipinstall