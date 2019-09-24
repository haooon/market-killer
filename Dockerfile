FROM python:3.6
ENV PATH /usr/local/bin:$PATH
RUN pip install -r ./pipinstall