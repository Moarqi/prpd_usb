FROM python:3.9-slim

# set the working directory in the container
WORKDIR /prpd

# copy the dependencies file to the working directory
# COPY requirements.txt .

# install dependencies
COPY . /prpd

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install /prpd

# copy the content of the local src directory to the working directory

# command to run on container start
CMD [ "prpd_usb", "-vvv", "prometheus"] 