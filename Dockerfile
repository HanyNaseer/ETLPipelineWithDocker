# use the official python image
FROM python:3.9

# set the workinf directory
WORKDIR /app

# install necessary python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of your application code
COPY . .

# set the entry point for Airflow
ENTRYPOINT [ "airflow" ]