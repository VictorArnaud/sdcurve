# Build an debian image
FROM python:3.6

# Install SO dependecies
RUN apt-get update && apt-get install -y \
    python3-dev \
    python3-pip \
    libpq-dev \
    python3-setuptools \
    gettext \
    vim \
    build-essential \
    apt-utils

# Install pip dependecies
RUN pip3 install --upgrade pip

# Insert Enviroment variable
ENV MODE_ENVIROMENT=development

# Create software folder
ADD . /software
WORKDIR /software
RUN pip3 install -r requirements.txt

# Run the dev script before and after any command
RUN chmod +x compose/local/local.sh
ENTRYPOINT ["compose/local/local.sh"]

# Run the server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
